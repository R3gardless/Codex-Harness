---
name: harness-frontend
description: Design and implement modern, coherent, accessible web UI with explicit tone, user flows, responsive states, and usable interactions. Use for frontend features or UI/UX improvement.
---

# Frontend with a clear visual direction

Start from the user, their primary task, content density, device, and the existing
design system. Write a short design direction: three tone words, the primary
action, information hierarchy, and the few visual choices supporting it. Respect
an established brand; do not redesign unrelated screens.

When no direction exists, use a calm, contemporary baseline: strong typography,
generous but purposeful spacing, restrained surfaces, one purposeful accent, and
consistent alignment. Avoid defaulting to gradients, excessive cards, tiny gray
text, ornamental charts, or animations without a useful role. An operational
screen should make the next action and current state obvious.

Define reusable tokens for color roles, typography, spacing, radii, and elevation
before repeated styling. The optional [token seed](assets/tokens.css) is a starting
point, not a required theme. Adjust it to the product and verify contrast.
Use the existing component library. For a new compatible React stack, prefer
Base UI with custom tokens for a distinct visual identity, or HeroUI v3 when
a cohesive ready-styled system better fits the delivery scope.
Do not force React, Tailwind, or a new design system into another stack.

Design the complete interaction:
- Clear navigation and one dominant action per task area; avoid needless steps.
- Loading, empty, error, retry, success, and disabled states where relevant.
- Explicit form labels, inline validation, retained user input, and useful errors.
- Destructive actions need appropriate confirmation or recovery. Prevent duplicate
  submission and represent pending actions accurately.
- Semantic HTML, keyboard access, visible focus, proper dialog focus management,
  reduced motion, and meaningful non-color indicators. Avoid custom ARIA when a
  native element fits. Check applicable WCAG criteria rather than claiming a full
  accessibility audit from a quick scan.
- Responsive layout, long text, realistic data, overflow, and touch ergonomics.

For React, check data waterfalls, unstable list keys, unnecessary client state,
and large client bundles before micro-optimizing renders. Preserve framework
server/client boundaries and never expose server secrets in the client bundle.

Use documentation MCPs only for version-specific public technical questions.
Component libraries provide building blocks, not a product design. Inspect
dependencies and proposed files before adding a component. Public HeroUI docs
and its MCP do not grant access to paid HeroUI Pro components.

Verify interaction semantics with the project's component tests and check build
and types. Give manual preview steps for layout, keyboard use, and the main flow;
do not run browser/Computer Use automation unless explicitly permitted. Mark
unobserved visual checks as unverified.

Optional references, read only for the relevant uncertainty:
- [W3C accessibility criteria](https://www.w3.org/WAI/WCAG22/quickref/)
- [Vercel web interface guidelines](https://github.com/vercel-labs/web-interface-guidelines)
- [Vercel React performance skill](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices)
- [Base UI](https://base-ui.com/react/overview/about)
- [HeroUI v3](https://heroui.com/en/docs/react/releases/v3-0-0)
