import importlib.util
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from install_harness import START, plan_install, apply_changes
from export_mcp import export_server


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.target = Path(self.temp.name) / "project"
        self.target.mkdir()

    def test_cli_preview_does_not_write(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/install_harness.py"),
                                 "--target", str(self.target)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(list(self.target.iterdir()), [])

    def test_preserves_instructions_and_other_skills(self):
        original = b"# Host\r\nKeep required API names.\r\n"
        (self.target / "AGENTS.md").write_bytes(original)
        other = self.target / ".agents/skills/custom/SKILL.md"
        other.parent.mkdir(parents=True)
        other.write_text("existing custom skill")
        apply_changes(plan_install(self.target))
        result = (self.target / "AGENTS.md").read_bytes()
        self.assertTrue(result.startswith(original))
        self.assertEqual(result.count(START.encode()), 1)
        self.assertEqual(other.read_text(), "existing custom skill")
        self.assertEqual(len(list((self.target / ".agents/skills").glob("harness-*/SKILL.md"))), 12)

    def test_reinstall_is_noop(self):
        apply_changes(plan_install(self.target))
        paths = [p for p in self.target.rglob("*") if p.is_file()]
        before = {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in paths}
        self.assertEqual(plan_install(self.target), [])
        apply_changes(plan_install(self.target))
        self.assertEqual(before, {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in paths})

    def test_skill_conflict_prevents_all_writes(self):
        conflict = self.target / ".agents/skills/harness-verify/SKILL.md"
        conflict.parent.mkdir(parents=True)
        conflict.write_text("user edits")
        with self.assertRaisesRegex(ValueError, "differs"):
            plan_install(self.target)
        self.assertEqual(conflict.read_text(), "user edits")
        self.assertFalse((self.target / "AGENTS.md").exists())
        self.assertFalse((self.target / ".agents/skills/harness-build").exists())

    def test_changed_managed_block_is_preserved(self):
        apply_changes(plan_install(self.target))
        path = self.target / "AGENTS.md"
        original = path.read_bytes().replace(b"Engineering harness", b"Edited harness")
        path.write_bytes(original)
        with self.assertRaisesRegex(ValueError, "block differs"):
            plan_install(self.target)
        self.assertEqual(path.read_bytes(), original)

    def test_symlink_directory_is_rejected(self):
        outside = Path(self.temp.name) / "outside"
        outside.mkdir()
        (self.target / ".agents").symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlink"):
            plan_install(self.target)
        self.assertEqual(list(outside.iterdir()), [])

    def test_source_inside_target_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "outside"):
            plan_install(ROOT)

    def test_install_does_not_apply_mcp_or_copy_docs(self):
        apply_changes(plan_install(self.target))
        self.assertFalse((self.target / ".codex").exists())
        self.assertFalse((self.target / "mcp").exists())
        self.assertFalse((self.target / "docs").exists())

    def test_changed_file_after_plan_is_not_overwritten(self):
        changes = plan_install(self.target)
        (self.target / "AGENTS.md").write_text("concurrent user edit")
        with self.assertRaisesRegex(ValueError, "changed since"):
            apply_changes(changes)
        self.assertFalse((self.target / ".agents").exists())


@unittest.skipUnless(importlib.util.find_spec("tomllib"), "Requires Python 3.11+ for TOML")
class ExportTests(unittest.TestCase):
    def test_exports_only_selected_server(self):
        result = export_server("aws_knowledge")
        self.assertEqual(list(result["mcpServers"]), ["aws_knowledge"])
        self.assertEqual(result["mcpServers"]["aws_knowledge"]["type"], "http")

    def test_resource_exports_preserve_restrictions(self):
        for name in ("aws_resources", "azure_resources"):
            server = export_server(name)["mcpServers"][name]
            self.assertIn("--read-only", server["args"])
            self.assertNotIn("enabled", server)
        self.assertIn("group", export_server("azure_resources")["mcpServers"]["azure_resources"]["args"])

    def test_unknown_server_fails(self):
        with self.assertRaises(ValueError):
            export_server("all")


if __name__ == "__main__":
    unittest.main()
