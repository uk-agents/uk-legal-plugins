---
name: plain-language-letters
description: >
  Reference: DEPRECATED — use `/legal-clinic-uk:client-letter` for routine
  correspondence or `/legal-clinic-uk:status client` for substantive updates.
  Split into two more focused skills during the v1 build. Kept as a redirect
  for migration.
user-invocable: false
---

# [DEPRECATED] Plain-Language Letters → see `/legal-clinic-uk:client-letter` and `/legal-clinic-uk:status client`

This skill was split during the v1 build:

- **Routine correspondence** (appointment confirms, document requests, brief "we filed it" updates) → `skills/client-letter/` — use `/legal-clinic-uk:client-letter [type]`

- **Substantive client status updates** → `skills/status/` in client-facing mode — use `/legal-clinic-uk:status client`

Both apply the plain-language standards (plain English, reading level, no jargon) from CLAUDE.md, and both include the required sign-off identifying the student and the supervising solicitor or barrister per SRA client care obligations.

See the respective SKILL.md files for full workflows.
