# Installation Instructions (For LLMs)

These instructions are designed to be followed by an LLM to self-install the IEEE Citation Generator skill in either Claude Code or Codex.

After installation, the skill should save formatted citations as `.docx` files by default. The conversation output remains plain text, but the Word document is the canonical deliverable.

The saved Word document should format citations as Times New Roman, justified paragraphs, curly quotes around article and paper titles, en dashes for page ranges, italic journal and conference venue names, and superscript ordinal suffixes such as `st`, `nd`, `rd`, and `th`.

## Prerequisites

- Claude Code or Codex installed and configured
- `curl` available in the terminal
- Internet access to fetch files from GitHub

## Option A: Install for Claude Code

### Step 1: Create required directories

```bash
mkdir -p ~/.claude/skills/ieee-citation-data
mkdir -p ~/.claude/commands
```

### Step 2: Download the command file

```bash
curl -fSL -o ~/.claude/commands/ieee-cite.md \
  "https://raw.githubusercontent.com/Zwl20085/ieee-citation-generator/master/commands/ieee-cite.md"
```

### Step 3: Download the skill file

```bash
curl -fSL -o ~/.claude/skills/ieee-citation-generator.md \
  "https://raw.githubusercontent.com/Zwl20085/ieee-citation-generator/master/skills/ieee-citation-generator.md"
```

### Step 4: Download the abbreviation data files

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

### Step 5: Verify Claude installation

```bash
ls -la ~/.claude/commands/ieee-cite.md
ls -la ~/.claude/skills/ieee-citation-generator.md
ls -la ~/.claude/skills/ieee-citation-data/
```

Expected output: 5 files total - 1 command `.md` file, 1 skill `.md` file, and 3 `.json` data files.

### Step 6: Test in Claude Code

```text
/ieee-cite Attention Is All You Need
```

The skill should produce a properly formatted IEEE citation with full metadata in chat and save `ieee_citations.docx` in the working directory. The saved Word file should use Times New Roman, justified paragraphs, italic venue names for journals and conferences, and superscript ordinal suffixes.

## Option B: Install for Codex

### Step 1: Create required directories

```bash
mkdir -p ~/.codex/skills/ieee-citation-generator/data
```

### Step 2: Download the Codex skill file

```bash
curl -fSL -o ~/.codex/skills/ieee-citation-generator/SKILL.md \
  "https://raw.githubusercontent.com/Zwl20085/ieee-citation-generator/master/codex/ieee-citation-generator/SKILL.md"
```

### Step 3: Download the abbreviation data files

```bash
curl -fSL -o ~/.codex/skills/ieee-citation-generator/data/journal-abbreviations.json \
  "https://raw.githubusercontent.com/Zwl20085/ieee-citation-generator/master/data/journal-abbreviations.json"
```

```bash
curl -fSL -o ~/.codex/skills/ieee-citation-generator/data/conference-abbreviations.json \
  "https://raw.githubusercontent.com/Zwl20085/ieee-citation-generator/master/data/conference-abbreviations.json"
```

```bash
curl -fSL -o ~/.codex/skills/ieee-citation-generator/data/publisher-templates.json \
  "https://raw.githubusercontent.com/Zwl20085/ieee-citation-generator/master/data/publisher-templates.json"
```

### Step 4: Verify Codex installation

```bash
ls -la ~/.codex/skills/ieee-citation-generator/SKILL.md
ls -la ~/.codex/skills/ieee-citation-generator/data/
```

Expected output: 4 files total - 1 `SKILL.md` file and 3 `.json` data files.

### Step 5: Test in Codex

Ask Codex to use the installed skill, for example:

```text
Use ieee-citation-generator on this file: path/to/my-references.txt
```

or

```text
Format these references in IEEE style and save the result as a Word document.
```

The skill should produce formatted IEEE citations in chat and save a `.docx` output file in the working directory. The saved Word file should use Times New Roman, justified paragraphs, italic venue names for journals and conferences, and superscript ordinal suffixes.

## Uninstallation

### Claude Code

```bash
rm ~/.claude/commands/ieee-cite.md
rm ~/.claude/skills/ieee-citation-generator.md
rm -rf ~/.claude/skills/ieee-citation-data/
```

### Codex

```bash
rm -rf ~/.codex/skills/ieee-citation-generator/
```

## Updating

To update to the latest version, re-run the relevant download steps for your platform. The files will be overwritten with the latest versions.

## Troubleshooting

- Claude skill not appearing: Ensure `~/.claude/commands/ieee-cite.md` exists and restart Claude Code if needed.
- Codex skill not appearing: Ensure `~/.codex/skills/ieee-citation-generator/SKILL.md` exists in a folder named after the skill.
- Abbreviation data not loading: Verify the platform-specific data directory path matches the instructions above.
- `curl` fails: Check your internet connection and ensure the GitHub repository is accessible.
- Permission denied: Ensure the installed files are readable by your current user.
- Output opens with the wrong formatting: Open the generated `.docx` file in Word and verify Times New Roman, justification, curly quotes, en dashes, venue italics, and superscript ordinal suffixes rather than relying on a plain-text editor preview.
- Output shows `?` instead of quotes or page dashes: Treat that as punctuation corruption. Replace the affected characters with curly quotes `“ ”` and en dashes `–`, then verify the corrected citation before returning it.
- Output seems to drop authors: Re-run the metadata verification from the title match and rebuild the author list from the authoritative source before returning the citation.

## Platform Notes

- macOS and Linux: `~` expands to your home directory automatically.
- Windows (Git Bash or WSL): `~` expands to your user home directory for either toolchain.
- Claude Code on Windows typically uses `%USERPROFILE%\\.claude\\`.
- Codex on Windows typically uses `%USERPROFILE%\\.codex\\`.
