---
name: harness-frontend
description: Plan tone and UI/UX before implementing accessible frontend features with light/dark themes and responsive mobile, tablet, and desktop layouts. Use for frontend features or UI/UX improvement.
---

# Frontend with a clear visual direction

Before coding UI, inspect the user, their primary task, content density, devices,
and existing design system. Write a short design brief in the existing work note
or response: three tone words, primary action, information hierarchy, navigation
and task flow, screen outline or wireframe, and interaction states. Specify theme
and responsive behavior at this stage. A small change needs only a brief delta
to the established design, not a new design document or approval gate. Respect
an established brand; do not redesign unrelated screens. Identify assumptions
and ask only about gaps that would materially change the implementation.

When no direction exists, use a calm, contemporary baseline: strong typography,
generous but purposeful spacing, restrained surfaces, one purposeful accent, and
consistent alignment. Avoid defaulting to gradients, excessive cards, tiny gray
text, ornamental charts, or animations without a useful role. An operational
screen should make the next action and current state obvious.

Define reusable tokens for color roles, typography, spacing, radii, and elevation
before repeated styling. The optional [token seed](assets/tokens.css) is a starting
point for light/dark palettes, not a required theme or a complete theme controller.
Adjust it to the product and verify contrast.
Use the existing component library. For a new compatible React stack, prefer
Base UI with custom tokens for a distinct visual identity, or HeroUI v3 when
a cohesive ready-styled system better fits the delivery scope.
Do not force React, Tailwind, or a new design system into another stack.

Design the complete interaction before implementation:

- Clear navigation and one dominant action per task area; avoid needless steps.
- Loading, empty, error, retry, success, and disabled states where relevant.
- Explicit form labels, inline validation, retained user input, and useful errors.
- Destructive actions need appropriate confirmation or recovery. Prevent duplicate
  submission and represent pending actions accurately.
- Semantic HTML, keyboard access, visible focus, proper dialog focus management,
  reduced motion, and meaningful non-color indicators. Avoid custom ARIA when a
  native element fits. Check applicable WCAG criteria rather than claiming a full
  accessibility audit from a quick scan.
- Mobile, tablet, and desktop layouts with content-driven breakpoints. Define
  navigation changes, column stacking, table overflow, and dialog sizing. Keep
  key actions reachable by touch; test long text, realistic data, zoom, and narrow
  screens without accidental page-wide horizontal scrolling.

Support light and dark mode unless explicit project requirements say otherwise.
Use semantic tokens for all surfaces, text, borders, focus, and feedback states;
include dialogs, menus, charts, images, and native controls. Follow the OS theme
by default and offer an accessible light/dark/system preference using the existing
settings UI or a small control. Persist explicit choices with the project's
mechanism; system mode follows OS changes. Account for unavailable storage,
initial rendering, and SSR/hydration so the page does not flash the wrong theme.
Do not add a second theme controller when the framework already provides one.

For React, check data waterfalls, unstable list keys, unnecessary client state,
and large client bundles before micro-optimizing renders. Preserve framework
server/client boundaries and never expose server secrets in the client bundle.

Use documentation MCPs only for version-specific public technical questions.
Component libraries provide building blocks, not a product design. Inspect
dependencies and proposed files before adding a component. Public HeroUI docs
and its MCP do not grant access to paid HeroUI Pro components.

Verify interaction semantics with the project's component tests and check build
and types. Check theme selection, persistence, system fallback, and material UI
states. Give a manual preview matrix covering light/dark at mobile, tablet, and
desktop sizes, plus keyboard use, contrast, overflow, and the main flow;
do not run browser/Computer Use automation unless explicitly permitted. Mark
unobserved visual checks as unverified.

Optional references, read only for the relevant uncertainty:
- [W3C accessibility criteria](https://www.w3.org/WAI/WCAG22/quickref/)
- [Vercel web interface guidelines](https://github.com/vercel-labs/web-interface-guidelines)
- [Vercel React performance skill](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices)
- [Base UI](https://base-ui.com/react/overview/about)
- [HeroUI v3](https://heroui.com/en/docs/react/releases/v3-0-0)
