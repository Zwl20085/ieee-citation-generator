# Installation Instructions (For LLMs)

These instructions are designed to be followed by an LLM (e.g., Claude Code) to self-install the IEEE Citation Generator skill.

## Prerequisites

- Claude Code CLI installed and configured
- `curl` available in the terminal
- Internet access to fetch files from GitHub

## Installation Steps

Follow these steps in order. Execute each command using the Bash tool.

### Step 1: Create the skill data directory

```bash
mkdir -p ~/.claude/skills/ieee-citation-data
```

### Step 2: Download the skill file

```bash
curl -fSL -o ~/.claude/skills/ieee-citation-generator.md \
  "https://raw.githubusercontent.com/Zwl20085/ieee-citation-generator/master/skills/ieee-citation-generator.md"
```

### Step 3: Download the abbreviation data files

Run all three commands:

```bash
curl -fSL -o ~/.claude/skills/ieee-citation-data/journal-abbreviations.json \
  "https://raw.githubusercontent.com/Zwl20085/ieee-citation-generator/master/data/journal-abbreviations.json"
```

```bash
curl -fSL -o ~/.claude/skills/ieee-citation-data/conference-abbreviations.json \
  "https://raw.githubusercontent.com/Zwl20085/ieee-citation-generator/master/data/conference-abbreviations.json"
```

```bash
curl -fSL -o ~/.claude/skills/ieee-citation-data/publisher-templates.json \
  "https://raw.githubusercontent.com/Zwl20085/ieee-citation-generator/master/data/publisher-templates.json"
```

### Step 4: Verify installation

Check that all files exist:

```bash
ls -la ~/.claude/skills/ieee-citation-generator.md
ls -la ~/.claude/skills/ieee-citation-data/
```

Expected output: 4 files total — 1 skill `.md` file and 3 `.json` data files.

### Step 5: Test the skill

Invoke the skill by typing in Claude Code:

```
/ieee-cite Attention Is All You Need
```

The skill should produce a properly formatted IEEE citation with full metadata.

## Uninstallation

To remove the skill:

```bash
rm ~/.claude/skills/ieee-citation-generator.md
rm -rf ~/.claude/skills/ieee-citation-data/
```

## Updating

To update to the latest version, re-run Steps 2 and 3. The files will be overwritten with the latest versions.

## Troubleshooting

- **Skill not appearing**: Restart Claude Code after installation
- **Abbreviation data not loading**: Verify the data directory path matches `~/.claude/skills/ieee-citation-data/`
- **curl fails**: Check your internet connection and ensure the GitHub repository is accessible
- **Permission denied**: Run `chmod 644 ~/.claude/skills/ieee-citation-generator.md` and `chmod 644 ~/.claude/skills/ieee-citation-data/*.json`

## Platform Notes

- **macOS / Linux**: `~` expands to your home directory automatically
- **Windows (Git Bash / WSL)**: `~` expands to `C:\Users\<username>` in Git Bash or `/home/<username>` in WSL. Claude Code on Windows uses `%USERPROFILE%\.claude\skills\`
