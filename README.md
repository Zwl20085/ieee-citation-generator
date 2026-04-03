# IEEE Citation Generator for Claude Code and Codex

An IEEE citation skill package that supports both Claude Code and Codex. It generates properly formatted IEEE transaction-style citations from paper titles, raw citation text, or plain-text reference files, then saves the polished result as a Word document.

## Platform Support

- Claude Code: supported through the slash command in `commands/ieee-cite.md` plus the Claude-oriented skill file in `skills/ieee-citation-generator.md`
- Codex: supported through the packaged Codex skill directory in `codex/ieee-citation-generator/`

## LLM Installation

For AI assistants, install by following:

```text
https://raw.githubusercontent.com/Zwl20085/ieee-citation-generator/master/installation.md
```

Then choose the Claude Code or Codex installation section that matches your environment.

## What It Does

- Takes paper titles, partial citations, or messy reference text as input
- Uses the title as the primary anchor and verifies metadata from search results before formatting
- Rebuilds the authoritative IEEE author list instead of trusting truncated input author strings
- Looks up or re-checks metadata such as authors, year, DOI, volume, and pages via web search
- Formats everything in correct IEEE citation style
- Handles journal articles, conference papers, books, websites, and arXiv preprints
- Uses standard IEEE abbreviations such as `IEEE Trans. Power Electron.` and `in Proc. IEEE Int. Conf. Elect. Mach. Drives`
- Works with non-IEEE publishers while still formatting in IEEE style
- Saves formatted citations to a `.docx` file by default so Word preserves IEEE-required punctuation and formatting reliably

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

## Output

Formatted citations are shown in chat as plain text and saved to a `.docx` file:

```text
[1] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image recognition,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Las Vegas, NV, USA, Jun. 2016, pp. 770–778.

[2] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, “BERT: Pre-training of deep bidirectional transformers for language understanding,” in Proc. Conf. North Amer. Ch. Assoc. Comput. Linguist.: Hum. Lang. Technol. (NAACL-HLT), Minneapolis, MN, USA, Jun. 2019, pp. 4171–4186.

[3] “PyTorch documentation.” PyTorch. https://pytorch.org/docs/stable/index.html (accessed Apr. 3, 2026).
```

Saved file names:

- Direct input -> `ieee_citations.docx`
- File input -> `<input_basename>_ieee.docx`

The saved Word document should format each citation as:

- One justified paragraph per citation
- Visible spacing between citation paragraphs
- Times New Roman for all text
- Curly quotation marks `“ ”` around article and paper titles
- En dash `–` for page ranges, never hyphen `-`
- Italic journal and conference venue names only
- Superscript ordinal suffixes such as `st`, `nd`, `rd`, and `th`
- Never substitute `?` for quotation marks or page-range dashes
- Use exactly one space between the closing title quote and the following venue text

The chat response should also keep a blank line between adjacent references so they do not run together visually.

Word output is the default because many plain-text editors and clipboard paths silently replace or mangle the punctuation IEEE references require, especially title quotes and page-range dashes.

## Supported Citation Types

| Type | Example Source |
|---|---|
| Journal article | IEEE Transactions, ACM Transactions, Nature, Science, Elsevier journals |
| Conference paper | IEEE ECCE, CVPR, NeurIPS, ICML, ICLR |
| Book | Any publisher |
| Book chapter | Springer LNCS and similar series |
| Website | Any URL |
| arXiv preprint | arXiv.org papers |
| Standard | IEEE, ISO, IEC standards |
| Patent | Any country |

## Repository Layout

- `commands/ieee-cite.md` - Claude Code slash command
- `skills/ieee-citation-generator.md` - Claude Code skill instructions
- `codex/ieee-citation-generator/SKILL.md` - Codex skill instructions
- `data/` - shared abbreviation and formatting data for both platforms
- `tests/test-cases.md` - manual regression scenarios
- `tests/test_skill_regressions.py` - automated prompt-package regression checks

## Regression Notes

Two important regressions are now explicitly guarded:

1. Punctuation corruption such as `?Incorporating skew...` or `pp. 816?818` must be normalized to `“Incorporating skew...` and `pp. 816–818`.
2. Truncated author lists such as the Ref. 16 example must be rebuilt from authoritative metadata, yielding `J. Chen, W. Hua, L. Shao and Z. Wu`.

## Manual Installation

### Claude Code

1. Copy `commands/ieee-cite.md` to `~/.claude/commands/`
2. Copy `skills/ieee-citation-generator.md` to `~/.claude/skills/`
3. Copy the `data/` directory contents to `~/.claude/skills/ieee-citation-data/`

### Codex

1. Create `~/.codex/skills/ieee-citation-generator/`
2. Copy `codex/ieee-citation-generator/SKILL.md` into that directory as `SKILL.md`
3. Copy the `data/` directory into `~/.codex/skills/ieee-citation-generator/data/`

## IEEE Citation Format Reference

This skill follows the [IEEE Reference Guide](https://ieeeauthorcenter.ieee.org/wp-content/uploads/IEEE-Reference-Guide.pdf). Key rules:

- Author names use initials before surnames
- No Oxford comma for 1 to 3 authors
- Oxford comma before `and` for 4 to 6 authors
- Use `et al.` for 7 or more authors
- Article titles use curly quotes and sentence case
- Use exactly one space after the closing title quote before the venue text
- Journal and conference names are abbreviated per IEEE standards
- En dash is required for page ranges everywhere
- Saved Word output uses Times New Roman and justified paragraphs
- Journal and conference venue names are italicized in the Word document
- Ordinal suffixes such as `st`, `nd`, `rd`, and `th` are superscripted in the Word document
- If punctuation degrades into `?` or mojibake, normalize it to curly quotes and en dashes before returning or saving the citation

## License

MIT
