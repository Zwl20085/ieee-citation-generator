# IEEE Citation Generator for Claude Code

A Claude Code skill that generates properly formatted IEEE transaction-style citations from paper titles, raw citation text, or text files.

## LLM Installation

> **For AI assistants**: To install this skill, fetch and follow the instructions at:
> ```
> https://raw.githubusercontent.com/Zwl20085/ieee-citation-generator/master/installation.md
> ```
> Read that file and execute each step sequentially.

## What It Does

- Takes paper titles, partial citations, or messy reference text as input
- Looks up missing metadata (authors, year, DOI, volume, pages) via web search
- Formats everything in correct IEEE citation style
- Handles journal articles, conference papers, books, websites, and arXiv preprints
- Uses standard IEEE abbreviations (e.g., "IEEE Trans. Power Electron.", "in Proc. IEEE Int. Conf. Elect. Mach. Drives")
- Works with non-IEEE publishers (ACM, Elsevier, Springer, etc.) — still formats in IEEE style
- Outputs to a `.txt` file

## Usage

### Direct input (paper title)
```
/ieee-cite Attention Is All You Need
```

### Direct input (messy citation)
```
/ieee-cite Vaswani et al., Attention Is All You Need, NeurIPS 2017
```

### File input (batch processing)
```
/ieee-cite path/to/my-references.txt
```

Where `my-references.txt` contains one citation per line:
```
Deep Residual Learning for Image Recognition
BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
https://pytorch.org/docs/stable/index.html
```

### Output

Formatted citations saved to a `.txt` file:
```
[1] K. He, X. Zhang, S. Ren, and J. Sun, "Deep residual learning for image recognition," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Las Vegas, NV, USA, 2016, pp. 770–778, doi: 10.1109/CVPR.2016.90.
[2] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, "BERT: Pre-training of deep bidirectional transformers for language understanding," in Proc. Conf. North Amer. Ch. Assoc. Comput. Linguist.: Hum. Lang. Technol. (NAACL-HLT), Minneapolis, MN, USA, 2019, pp. 4171–4186.
[3] "PyTorch documentation." PyTorch. https://pytorch.org/docs/stable/index.html (accessed Apr. 3, 2026).
```

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

## Abbreviation Coverage

The skill includes abbreviation tables for:
- **100+ IEEE journal names** (all major IEEE Transactions, Journals, Letters, Magazines)
- **30+ major conferences** (IEEE, ACM, NeurIPS, ICML, etc.)
- **100+ word-level abbreviation rules** for composing abbreviations for unknown venues
- **15+ publisher-specific formatting quirks** (ACM, Elsevier, Springer, MDPI, etc.)

### Extending Abbreviations

To add custom abbreviations, edit the JSON files in `~/.claude/skills/ieee-citation-data/`:
- `journal-abbreviations.json` — add `"Full Name": "Abbrev. Name"` entries
- `conference-abbreviations.json` — add to `full_conference_names` or `word_abbreviations`

## Manual Installation

If you prefer to install manually:

1. Copy `skills/ieee-citation-generator.md` to `~/.claude/skills/`
2. Copy the `data/` directory contents to `~/.claude/skills/ieee-citation-data/`

```bash
# Clone the repo
git clone https://github.com/Zwl20085/ieee-citation-generator.git
cd ieee-citation-generator

# Install
cp skills/ieee-citation-generator.md ~/.claude/skills/
mkdir -p ~/.claude/skills/ieee-citation-data/
cp data/*.json ~/.claude/skills/ieee-citation-data/
```

## IEEE Citation Format Reference

This skill follows the [IEEE Reference Guide](https://ieeeauthorcenter.ieee.org/wp-content/uploads/IEEE-Reference-Guide.pdf) for formatting. Key rules:

- Author names: initials before surname (e.g., "J. K. Smith")
- "and" before the last author; "et al." for 7+ authors
- Article titles in double quotes, sentence case
- Journal/conference names abbreviated per IEEE standards
- En-dash (–) for page ranges
- DOI formatted as `doi: 10.xxxx/xxxxx.`
- Month abbreviations: Jan., Feb., Mar., Apr., May, Jun., Jul., Aug., Sep., Oct., Nov., Dec.

## License

MIT
