# R223D Component Strip Density Check

## Rule

```text
daily_prep max_visible_components = 3
quick_prep max_visible_components = 2
precision_prep component suggestions appear after relevant decision context, not as a global shelf
```

## Strip Content

Each visible component card in the strip may show only:

```text
label + component_id
student problem short line
evidence output short line
media need icon/short phrase
confirm / replace / delete actions
```

The full `why_use`, teacher language, learning sheet, screen prompt, and media detail open in binding preview only after component focus.

## Blocked Pattern

```text
Showing 12 component buttons or a scrollable component marketplace.
```

## Density Pass

The strip passes only if it does not obscure the focused section card and does not require horizontal browsing to understand the lesson plan.
