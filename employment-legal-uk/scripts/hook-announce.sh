#!/usr/bin/env bash
# Debug hook for employment-legal — prints to stderr and logs full payload.
# Remove before merging to main (or keep for production observability).

EVENT="${1:-event}"

case "$EVENT" in
  start)     ICON="🚀"; LABEL="SessionStart"     ;;
  prompt)    ICON="💬"; LABEL="UserPromptSubmit" ;;
  pre-tool)  ICON="⚡"; LABEL="PreToolUse"       ;;
  post-tool) ICON="✅"; LABEL="PostToolUse"      ;;
  *)         ICON="🔔"; LABEL="$EVENT"           ;;
esac

printf '%s [employment-legal] %s\n' "$ICON" "$LABEL" >&2

# Derive plugin root from this script's own location — don't rely on
# ${PLUGIN_ROOT} being exported as an env var (Goose substitutes it in
# the command string only; Claude Code doesn't set it at all).
SELF_DIR="$(cd "$(dirname "$0")" && pwd)"
PLUGIN_DIR="$(cd "$SELF_DIR/.." && pwd)"

LOG="${PLUGIN_DIR}/last-event.log"
printf '=== %s %s ===\n' "$(date -Iseconds)" "$LABEL" >> "$LOG"
cat >> "$LOG"
printf '\n' >> "$LOG"
