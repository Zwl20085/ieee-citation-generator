# IEEE Citation Generator for Claude Code and Codex

An IEEE citation skill package that supports both Claude Code and Codex. It generates properly formatted IEEE transaction-style citations from paper titles, raw citation text, or plain-text reference files, then saves the polished result as a Word document.

## Platform Support

- **Claude Code**: supported through the slash command in `commands/ieee-cite.md` plus the Claude-oriented skill file in `skills/ieee-citation-generator.md`
- **Codex**: supported through the packaged Codex skill directory in `codex/ieee-citation-generator/`

## LLM Installation

> **For AI assistants**: To install this repository, fetch and follow the instructions at:
> ```
> https://raw.githubusercontent.com/Zwl20085/ieee-citation-generator/master/installation.md
> ```
> Then choose the Claude Code or Codex installation section that matches your environment.

## What It Does

- Takes paper titles, partial citations, or messy reference text as input
- Looks up missing metadata (authors, year, DOI, volume, pages) via web search
- Formats everything in correct IEEE citation style
- Handles journal articles, conference papers, books, websites, and arXiv preprints
- Uses standard IEEE abbreviations (e.g., "IEEE Trans. Power Electron.", "in Proc. IEEE Int. Conf. Elect. Mach. Drives")
- Works with non-IEEE publishers (ACM, Elsevier, Springer, etc.) while still formatting in IEEE style
- Saves formatted citations to a `.docx` file by default so Word preserves IEEE-required punctuation reliably

## Usage

### Claude Code

```text
/ieee-cite Attention Is All You Need
```

```text
/ieee-cite path/to/my-references.txt
```

### Codex

Install the Codex skill, then invoke it naturally by asking for IEEE-formatted citations or by mentioning `ieee-citation-generator`.

Example prompts:

```text
Use ieee-citation-generator on this file: path/to/my-references.txt
```

```text
Format these references in IEEE style and save the result as a Word document.
```

The batch file can be any readable plain-text citation list, but `.txt` remains the recommended format for inputs.

Where `my-references.txt` contains one citation per line:

```text
Deep Residual Learning for Image Recognition
BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
https://pytorch.org/docs/stable/index.html
```

### Output

Formatted citations are shown in chat as plain text and saved to a `.docx` file:

```text
[1] K. He, X. Zhang, S. Ren, and J. Sun, "Deep residual learning for image recognition," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Las Vegas, NV, USA, Jun. 2016, pp. 770-778.
[2] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, "BERT: Pre-training of deep bidirectional transformers for language understanding," in Proc. Conf. North Amer. Ch. Assoc. Comput. Linguist.: Hum. Lang. Technol. (NAACL-HLT), Minneapolis, MN, USA, Jun. 2019, pp. 4171-4186.
[3] "PyTorch documentation." PyTorch. https://pytorch.org/docs/stable/index.html (accessed Apr. 3, 2026).
```

Saved file names:
- Direct input -> `ieee_citations.docx`
- File input -> `<input_basename>_ieee.docx`

Word output is the default because many plain-text editors and clipboard paths silently replace or mangle the punctuation IEEE references require, especially title quotes and page-range dashes.

## Supported Citation Types

| Type | Example Source |
|------|--------------|
| Journal article | IEEE Trans., ACM Trans., Nature, Science, Elsevier journals |
| Conference paper | IEEE ECCE, CVPR, NeurIPS, ICML, ICLR |
| Book | Any publisher |
| Book chapter | Springer LNCS, etc. |
| Website | Any URL |
| arXiv preprint | arXiv.org papers |
| Standard | IEEE, ISO, IEC standards |
| Patent | Any country |

## Repository Layout

- `commands/ieee-cite.md` - Claude Code slash command
- `skills/ieee-citation-generator.md` - Claude Code skill instructions
- `codex/ieee-citation-generator/SKILL.md` - Codex skill instructions
- `data/` - shared abbreviation and formatting data for both platforms

## Abbreviation Coverage

The skill includes abbreviation tables for:
- **100+ IEEE journal names** (all major IEEE Transactions, Journals, Letters, Magazines)
- **30+ major conferences** (IEEE, ACM, NeurIPS, ICML, etc.)
- **100+ word-level abbreviation rules** for composing abbreviations for unknown venues
- **15+ publisher-specific formatting quirks** (ACM, Elsevier, Springer, MDPI, etc.)

### Extending Abbreviations

To add custom abbreviations:
- Claude Code installs use `~/.claude/skills/ieee-citation-data/`
- Codex installs use `~/.codex/skills/ieee-citation-generator/data/`

Edit:
- `journal-abbreviations.json` - add `"Full Name": "Abbrev. Name"` entries
- `conference-abbreviations.json` - add to `full_conference_names` or `word_abbreviations`

## Manual Installation

### Claude Code

1. Copy `commands/ieee-cite.md` to `~/.claude/commands/`
2. Copy `skills/ieee-citation-generator.md` to `~/.claude/skills/`
3. Copy the `data/` directory contents to `~/.claude/skills/ieee-citation-data/`

### Codex

1. Create `~/.codex/skills/ieee-citation-generator/`
2. Copy `codex/ieee-citation-generator/SKILL.md` into that directory as `SKILL.md`
3. Copy the `data/` directory into `~/.codex/skills/ieee-citation-generator/data/`

```bash
# Clone the repo
git clone https://github.com/Zwl20085/ieee-citation-generator.git
cd ieee-citation-generator

# Claude Code install
mkdir -p ~/.claude/commands ~/.claude/skills/ieee-citation-data
cp commands/ieee-cite.md ~/.claude/commands/
cp skills/ieee-citation-generator.md ~/.claude/skills/
cp data/*.json ~/.claude/skills/ieee-citation-data/

# Codex install
mkdir -p ~/.codex/skills/ieee-citation-generator/data
cp codex/ieee-citation-generator/SKILL.md ~/.codex/skills/ieee-citation-generator/SKILL.md
cp data/*.json ~/.codex/skills/ieee-citation-generator/data/
```

## IEEE Citation Format Reference

This skill follows the [IEEE Reference Guide](https://ieeeauthorcenter.ieee.org/wp-content/uploads/IEEE-Reference-Guide.pdf) for formatting. Key rules:

- Author names: initials before surname (e.g., "J. K. Smith")
- "and" before the last author; "et al." for 7+ authors
- Article titles in double quotes, sentence case
- Journal and conference names abbreviated per IEEE standards
- En dash for page ranges in the saved Word document
- DOI formatted as `doi: 10.xxxx/xxxxx.`
- Month abbreviations: Jan., Feb., Mar., Apr., May, Jun., Jul., Aug., Sep., Oct., Nov., Dec.

## License

MIT
