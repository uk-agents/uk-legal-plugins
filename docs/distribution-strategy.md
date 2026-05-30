# Distribution strategy

## Decision (locked 2026-05-30)

**Option C1 — single free public repo.** All 11 plugins stay at `uk-agents/uk-legal-plugins`, free, no premium fork. Maximum reach. No skill revenue this cycle.

This document records the reasoning, the four target ecosystems and what each can reach, the dual-manifest plugin format, and the future revenue paths kept open but not implemented.

## Why a single free repo (not a fork or paid tier)

Three options were on the table:

| Option | What it does | Why we passed |
|---|---|---|
| C1 (chosen) | All 11 plugins free, single repo | Maximum reach, no entitlement infra needed, supports the freemium "MCP server + skills" story |
| C2 | Fork into free public + premium private | Splits userbase; premium repo creates a partner-discovery problem; skill revenue is uncertain anyway |
| C3 | Two tiers in one repo with entitlement-gated install | Cleanest UX, but requires paywall service + license-check tooling that doesn't exist yet |

**Why C1 wins right now:**

1. **Skill revenue isn't the v1.1 monetisation path.** The session arc was about getting the lawyer workflows to actually work (ChatGPT dogfeed surfaced gaps). Monetisation comes later via:
   - Premium MCP server tier (rate limits, dedicated infra, SLA)
   - BOUCH advisory / consulting on custom plugin development for firms
   - Premium skill marketplace later, IF entitlement infra exists
2. **Splitting the userbase now creates a partner-discovery problem.** Lawyers find skills via the plugin marketplace; if "the good stuff" lives in a private repo they can't see, the free repo's discovery surface gets weakened.
3. **Entitlement infra (C3) is real work.** A paywall service + license-key validation + revocation flow + customer-support surface for failed entitlement checks. Cost > expected revenue this cycle.

The choice is reversible — if and when premium skill revenue becomes the right strategy, fork to C2 or build C3 then. Nothing here commits to C1 forever.

## The four target client ecosystems

Per the audit recorded in `/home/bch/.claude/plans/scalable-tickling-meadow.md`:

| Ecosystem | Reaches | MCP tools | MCP resources | MCP prompts | Skills (client-loaded) | Hooks | Agents |
|---|---|---|---|---|---|---|---|
| **ChatGPT consumer** | ~80M/week, broadest audience | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| **Claude Code** | Developer audience + lawyer-developers | ✓ | ✓ | ✓ | ✓ via `.claude-plugin/` | ✓ | ✓ |
| **Cowork (Anthropic)** | Anthropic collaborative env users | ✓ | ✓ | ✓ | ✓ same format as Claude Code | ✓ | ✓ |
| **OpenAI Codex CLI** | OpenAI developer audience | ✓ | ✓ | ✓ | ✓ via `.codex-plugin/` (same surfaces as Claude) | ✓ | ✓ |

**Critical implication:** ChatGPT (the highest-volume audience) sees **tools only**. Skills, plugins, prompts, resources — none reach ChatGPT users.

This means:
- **For ChatGPT users**: the MCP server's tool descriptions are the only workflow-teaching layer. See `uk-legal-mcp/docs/chatgpt-workflow-encoding.md`.
- **For Claude Code / Cowork / Codex users**: skills + tool descriptions both reach them. Skills carry the rich workflows; tool descriptions stay strong because (a) skill triggering depends on the agent reading them, (b) some workflows are still simple-enough to inline as tool composition without a skill.

## Dual-manifest plugin pattern

Each of the 11 plugins carries TWO plugin manifests pointing at the same `skills/` + `.mcp.json`:

```
<plugin-name>/
├── .claude-plugin/
│   └── plugin.json             # Claude Code + Cowork manifest
├── .codex-plugin/
│   └── plugin.json             # OpenAI Codex CLI manifest
├── .mcp.json                   # shared — referenced by both manifests
├── skills/                     # shared — referenced by both manifests
│   ├── <skill-1>/SKILL.md
│   ├── <skill-2>/SKILL.md
│   └── ...
├── agents/                     # optional, shared
├── commands/                   # optional, shared
├── hooks.json                  # optional, shared
├── CLAUDE.md                   # plugin-specific architecture notes
└── README.md
```

### Why both manifests on every plugin

Per OpenAI's `openai/plugins` repo README:

> Each plugin lives under `plugins/<name>/` with a required `.codex-plugin/plugin.json` manifest and optional companion surfaces such as `skills/`, `.app.json`, `.mcp.json`, plugin-level `agents/`, `commands/`, `hooks.json`, `assets/`, and other supporting files.

The companion surfaces are THE SAME as Claude Code's. The only fork is at the manifest layer — different manifest paths declare which client should pick up the plugin.

By shipping both manifests, one plugin definition reaches Claude Code + Cowork + Codex CLI without duplicating skills, agents, or .mcp.json files.

### plugin.json shape (Claude format)

```json
{
  "name": "employment-legal-uk",
  "version": "1.0.0",
  "description": "UK employment law plugin — contracts, status, dismissals, IR35, leave.",
  "author": "uk-agents",
  "homepage": "https://github.com/uk-agents/uk-legal-plugins"
}
```

### plugin.json shape (Codex format)

Verify against `openai/plugins` examples. Likely structurally similar; the field names may differ. To be confirmed at packaging time.

### Validation procedure

Per `uk-legal-plugins/CLAUDE.md`:

```bash
# Claude Code validation
cd <plugin>
/plugin validate

# Codex CLI validation
# (procedure TBD; verify at packaging time)
```

## Free public repo logistics

### Repo location

`uk-agents/uk-legal-plugins` (GitHub).

Mirror / development repo at `/home/bch/company/skills-uk/uk-legal-plugins` (working copy on Paul's machine).

### License

Per `LICENSE` in the repo (currently MIT or similar; verify).

### Marketplace listings

The plugin marketplace surface in Claude Code: `claude-plugin marketplace add github:uk-agents/uk-legal-plugins`.

The plugin marketplace surface in Codex CLI: verify via OpenAI's docs at packaging time.

### Update cadence

Plugins ship via GitHub — every push to `main` becomes the latest version. Versioning per `<plugin>/.claude-plugin/plugin.json:version`. Semantic versioning where the public contract changes.

### MCP server URL (the `.mcp.json` reference)

Every plugin's `.mcp.json` points at the deployed v1.1 production server:

```json
{
  "mcpServers": {
    "uk-legal": {
      "type": "http",
      "url": "https://uk-legal-mcp.fly.dev/mcp",
      "title": "UK Legal",
      "description": "UK case law, legislation, Hansard, bills, parliamentary votes, committees, HMRC guidance, and OSCOLA citation parsing."
    }
  }
}
```

Atomic in-place v1 → v1.1 upgrade means no plugin `.mcp.json` updates needed when v1.1 ships.

## What's intentionally NOT in this strategy

- **Premium tier infra.** No entitlement service, no license-check tooling, no paywall integration. Revisit if and when skill revenue becomes a target.
- **Per-firm custom plugins.** BOUCH consulting may produce per-firm plugins on contract — those don't ship in the public repo and have their own distribution model.
- **Sponsored skills.** No "Skill brought to you by <law firm>" pattern. Risk of legal-advice framing; out of scope.
- **Skills that encode legal positions / advice.** Per Phase D in the master plan: skills must be neutral procedural templates. No advocacy framing.

## Future revenue paths (recorded; not implemented this cycle)

1. **Premium MCP server tier**
   - Rate limits on the public server; private tier with higher limits + dedicated infra + SLA
   - Targets: law firms with > N developer agents calling the server, lawyer-tooling startups
   - Pricing model: tiered per-seat or per-call

2. **BOUCH advisory + custom plugins**
   - Per-engagement: build a custom plugin for a firm's specific workflows, ship in a private plugin repo for that firm
   - Pricing: project-based

3. **Premium skill marketplace**
   - Requires entitlement infra (out of scope C1)
   - Possible model: advanced skills (deep M&A diligence, structured litigation strategy, IP portfolio analytics) require a subscription
   - Revisit if/when entitlement service exists OR a marketplace partner (Anthropic marketplace, etc.) handles entitlement on our behalf

4. **Curated firm-specific marketplace partnerships**
   - Anthropic or OpenAI may surface UK-legal plugins to specific verticals
   - If so, free-public skills become discovery; partner pays for placement / curation

## Verification

For C1 to "work":

- All 11 plugins ship dual-manifest (Claude + Codex)
- Public connector `uk-legal-mcp.fly.dev/mcp` stays up + responds to ChatGPT direct connections
- Plugin marketplaces discoverable for both Claude Code + Codex CLI users
- New Phase B skills (5 of them per `skill-gaps-and-design.md`) ship inside the relevant free plugins, no entitlement gate

For C1 to "fail" (and the decision to revisit):

- Skill revenue would have been substantial AND the entitlement infra was cheaper to build than the revenue projected
- A premium partner (Anthropic / OpenAI) wants paid placement that requires a non-free tier

Neither condition is plausible this cycle. Decision stands.

## Cross-references

- `~/.claude/plans/scalable-tickling-meadow.md` — master plan
- `uk-legal-mcp/docs/v1.1-hardening-plan.md` — what's shipping in the MCP server v1.1
- `uk-legal-mcp/docs/chatgpt-workflow-encoding.md` — how workflows reach ChatGPT users (tools only)
- `uk-legal-plugins/docs/skill-gaps-and-design.md` — what's shipping in the new skill batch
- `uk-legal-plugins/CONNECTORS.md` — existing connector list (which MCPs ship with which plugins)
- `uk-legal-plugins/README.md` — public-facing plugin overview
