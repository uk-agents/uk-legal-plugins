# Quick Start

**60 seconds.** This gets you to using your plugins.

## Install in Claude Cowork

1. Personal plugins → Create plugin → Add marketplace → enter `uk-agents/uk-legal-plugins`
2. Go to Plugins → Personal and click `+` next to each plugin you want

Or upload a single plugin ZIP: Personal plugins → Create plugin → Upload plugin → select a ZIP from the [Releases page](https://github.com/uk-agents/uk-legal-plugins/releases).

## Install in Claude Code

1. **Open Claude Code** in your terminal.

2. **Add the marketplace.**
   ```
   claude plugin marketplace add uk-agents/uk-legal-plugins
   ```

3. **Install your plugin.** Pick the one that matches your work from the table below, then:
   ```
   claude plugin install employment-legal-uk@uk-legal-plugins
   ```

4. **⚠️ Restart Claude Code.** Close and reopen. This step is not optional — the plugin isn't live until you restart.

5. **Run setup.** Takes 2 minutes (quick start) or 10-15 minutes (full).
   ```
   /privacy-legal-uk:cold-start-interview
   ```

6. **Connect a research tool.** Citations are flagged unverified without one. In Cowork: Settings → Connectors → add CourtListener. In Claude Code: the plugin already lists the research MCP in its config; you'll be prompted to authorize it the first time a skill needs it.

## Install user-scoped, not project-scoped

When you run `/plugin install`, you may be asked whether to install for this project only or for all projects (user scope). **Pick user scope.**

It's counterintuitive: project scope feels safer. But project scope blocks the plugin from reading files outside the project folder — your outlines in Downloads, your contract in Documents, your client file in Dropbox. Most skills need to read your files. User scope doesn't give the plugin any extra access to your files — the plugin can only read files you explicitly point it at or that are in the current directory. It just means the plugin works from any folder instead of one.

If you already installed project-scoped and want to switch: `/plugin uninstall <plugin>`, then `/plugin install <plugin>@uk-legal-plugins` from your home directory.

## Which plugin is for me?

| You are a… | Install… | First command |
|---|---|---|
| Privacy lawyer / DPO | `privacy-legal-uk` | `/privacy-legal-uk:use-case-triage` |
| Commercial / contracts lawyer | `commercial-legal-uk` | `/commercial-legal-uk:review` |
| Corporate / M&A lawyer | `corporate-legal-uk` | `/corporate-legal-uk:diligence-issue-extraction` |
| Employment lawyer / HR counsel | `employment-legal-uk` | `/employment-legal-uk:wage-hour-qa` |
| Product counsel | `product-legal-uk` | `/product-legal-uk:is-this-a-problem` |
| IP lawyer / patent agent | `ip-legal-uk` | `/ip-legal-uk:clearance` |
| Litigator (in-house or firm) | `litigation-legal-uk` | `/litigation-legal-uk:matter-intake` |
| Regulatory / compliance counsel | `regulatory-legal-uk` | `/regulatory-legal-uk:reg-feed-watcher` |
| AI governance lead | `ai-governance-legal-uk` | `/ai-governance-legal-uk:use-case-triage` |
| Clinic supervisor (law school) | `legal-clinic-uk` | `/legal-clinic-uk:cold-start-interview` |
| Law student | `law-student-uk` | `/law-student-uk:cold-start-interview` |

## What you're installing

Each plugin learns your playbook through a setup interview, writes it to a practice profile file (`~/.claude/plugins/config/uk-legal-plugins/<plugin>/CLAUDE.md`), and every skill reads from it. The profile is yours — edit it, re-run setup, or tell a skill to update it.

**Every output is a draft for attorney review.** The plugins flag what they're unsure about, mark citations by source, and gate anything irreversible. A lawyer reviews, verifies, and takes responsibility. They make that review faster; they don't replace it.

## What's in the box

11 UK-jurisdiction legal plugins. The full reference is in [README.md](README.md).

## Stuck?

- **"Command not found"** after install → you forgot step 4. Restart Claude Code.
- **"Run setup first"** → run `/<plugin>:cold-start-interview` before any other command.
- **Citations flagged `[verify]`** → connect a research tool (step 6). Without one, every cite is from training data, not a current database.
- **"I can't read [file]"** → most often this means the plugin is project-scoped and the file is outside the project folder. See "Install user-scoped, not project-scoped" above — reinstall user-scoped or move the file into the project folder.
- **The plugin doesn't do X** → check the plugin's README for "What this plugin does not do," or browse `/plugins` in chat to see what's available.
