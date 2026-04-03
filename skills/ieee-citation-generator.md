# IEEE Citation Generator

Generate properly formatted IEEE transaction-style citations from paper titles, raw citation text, URLs, or plain-text citation files, then save the final references to a Word document.

## Trigger

Use this skill when the user invokes `/ieee-cite`, asks for IEEE-formatted references, mentions `ieee-citation-generator`, or wants a citation file converted into IEEE style.

## Inputs

- Direct text: one title, one citation, one URL, or several entries separated by blank lines or numbering
- File path: a readable plain-text citation list file containing one citation per non-empty line

## Workflow

### Step 1: Parse input

1. If the input looks like a readable file path, read the file and treat each non-empty line as a separate citation entry.
2. Otherwise, treat the input as one or more direct citation entries.

### Step 2: Classify each entry

For each citation entry, determine which case applies:

- Title only: perform a web lookup for full metadata
- Partial citation: fill in missing metadata with targeted lookup
- Full citation in another style: verify and reformat into IEEE
- Already IEEE-like: verify correctness and repair any problems

Treat the title as the authoritative anchor for the work. Do not trust the input author list, venue, date, volume, issue, pages, article number, or DOI without checking them against the best title match.

### Step 3: Resolve metadata carefully

Search strategy:

1. Search the exact title first.
2. Use the title match to verify or replace the author list and author order, publication date, venue title, volume, issue, pages or article number, and DOI when applicable.
3. If needed, search the title plus an author name.
4. Use DOI pages directly when available.
5. For arXiv works, check `arxiv.org` directly.

Author completeness is mandatory:

- Never keep a shortened or truncated input author list if the authoritative title match contains additional authors.
- If the input says `et al.` or lists only some authors, replace it with the correct IEEE author list built from the authoritative source.
- If the title match disagrees with the input author order, use the authoritative order.
- Before returning or saving the citation, explicitly verify that no author names were dropped during formatting.

### Step 4: Final verification pass

After generating each reference, re-check the result before returning or saving it.

- Re-check the author list and author order against the best available source.
- Prefer the title match over the input metadata whenever they disagree.
- Confirm the publication date is complete and correctly reflected in the citation.
- Check whether any information was lost during formatting, such as missing authors, pages, article numbers, venue details, city, country, month, or year.
- Confirm there is exactly one space after the reference number before the citation text.
- Confirm there is exactly one space between the closing title quote and the following journal, conference, book, or website text.
- If punctuation degrades into `?`, replacement glyphs, or mojibake, normalize it before returning or saving the citation.
- Treat a lone `?` as punctuation corruption only when context shows it is standing in for an opening quote, a closing quote, or a page-range dash.
- Do not leave placeholder `?` characters in the final citation where `“`, `”`, or `–` should appear.

### Step 5: Load local data files

Load these files before formatting:

- `~/.claude/skills/ieee-citation-data/journal-abbreviations.json`
- `~/.claude/skills/ieee-citation-data/conference-abbreviations.json`
- `~/.claude/skills/ieee-citation-data/publisher-templates.json`

### Step 6: Apply IEEE formatting rules

Return citations as plain text in chat. Save the canonical deliverable as a `.docx` file.

Apply these spacing rules everywhere:

- Use exactly one space between the reference number and the citation text.
- Use exactly one space between the closing title quote and the following journal, conference, book, or website text.
- When returning multiple references in chat, separate them with a blank line.
- In the saved Word document, keep one citation paragraph per reference and leave visible paragraph spacing between references.

The saved Word document should format citations as follows:

- Times New Roman for all citation text
- Fully justified paragraph alignment
- One citation paragraph per reference
- Curly quotation marks `“ ”` around article and paper titles, never straight ASCII `"` quotes
- En dash `–` for page ranges, never hyphen `-`
- Italic journal and conference venue names only
- Superscript ordinal suffixes such as `st`, `nd`, `rd`, and `th` wherever they appear
- Never emit `?` as a substitute for quotation marks, dashes, or other punctuation
- Never collapse the post-title space; forms like `,”IEEE` are invalid and must be `,” IEEE`

#### Journal article

```text
[N] A. B. Surname, C. D. Surname and E. F. Surname, “Title of article,” Abbrev. J. Name, vol. X, no. Y, pp. Z1–Z2, Mon. Year.
```

Rules:

- Format authors as initials plus surname.
- For 1 to 3 authors, do not use an Oxford comma before `and`.
- The 3-author form must be `M. Cheng, P. Han and Z. Wu`, not `M. Cheng, P. Han, and Z. Wu`.
- For 4 to 6 authors, use an Oxford comma before `and`.
- For 7 or more authors, list the first 6, then `et al.`
- Always use curly quotes `“ ”` around article and paper titles.
- Always use an en dash `–` for page ranges.
- Use article numbers as `Art. no. XXXXX` when pages are unavailable.
- Include a DOI only for early-access journal articles with no volume, issue, or pages yet.
- Italicize the journal venue name in the Word document.

#### Conference paper

```text
[N] A. B. Surname and C. D. Surname, “Title of paper,” in Proc. Abbrev. Conf. Name, City, Country, Mon. Year, pp. Z1–Z2.
```

Rules:

- Always include `in Proc.`
- Include city, country, and month when they can be verified.
- Do not include DOI for conference papers.
- Apply the same author-list punctuation rule as journal articles, including no Oxford comma for 3 authors.
- Italicize the conference venue name in the Word document.
- Superscript ordinal suffixes such as `24th` or `8th` in the Word document.

#### Book

```text
[N] A. B. Surname, Title of Book, Xth ed. City, Country: Publisher, Year.
```

Rules:

- Superscript ordinal suffixes such as `2nd ed.` or `3rd ed.` in the Word document.

#### Book chapter

```text
[N] A. B. Surname, “Chapter title,” in Title of Book, A. B. Editor, Ed. City, Country: Publisher, Year, pp. Z1–Z2.
```

#### Website

```text
[N] A. B. Surname. “Page title.” Website Name. URL (accessed Mon. Day, Year).
```

#### arXiv preprint

```text
[N] A. B. Surname and C. D. Surname, “Title,” arXiv preprint arXiv:XXXX.XXXXX, Year.
```

### Step 7: Number and output

1. Number citations sequentially as `[1]`, `[2]`, `[3]`, and so on.
2. Display all formatted citations to the user in plain text, with a blank line between references.
3. Save the formatted citations to a `.docx` file:
   - If input was a file such as `input.txt`, save as `input_ieee.docx` in the same directory.
   - If input was direct text, save as `ieee_citations.docx` in the current working directory.
   - Use the shared exporter script whenever it is available instead of hand-building the Word file ad hoc.
   - In this repository, the exporter lives at `scripts/export_ieee_docx.py`.
   - In a standalone Claude install, the exporter should live at `~/.claude/skills/export_ieee_docx.py`.
   - Run `python <exporter_path> <input_txt> [output_docx]` after the plain-text citations are finalized so journal and conference venue names are italicized and ordinal suffixes are superscripted consistently.
4. Before returning or saving the citations, confirm that no author names, publication-date fields, or other verified metadata were dropped during reformatting.

## Special handling

- Render all sources in IEEE style regardless of original publisher.
- Use `publisher-templates.json` for publisher-specific quirks such as article numbers or series formatting.
- If a title maps to multiple possible works, surface the ambiguity and ask the user to choose.
- Preserve input order when formatting multiple entries.

## Regression checkpoints

These regressions must be corrected if they appear in user input or intermediate output:

```text
[15] R. Wang, S. Pekarek, P. O'Regan, A. Larson, and R. van Maaren, “Incorporating skew in a magnetic equivalent circuit model of synchronous machines,” IEEE Trans. Energy Convers., vol. 30, no. 2, pp. 816–818, Jun. 2015.

[16] J. Chen, W. Hua, L. Shao and Z. Wu, “Modified magnetic equivalent circuit of double-stator single-rotor axial flux permanent magnet machine considering stator radial-end flux-leakage,” IET Elect. Power Appl., vol. 18, no. 2, pp. 195–207, 2024.
```

Never return the broken forms below:

```text
[15] ... ?Incorporating skew ... pp. 816?818 ...
[16] ... J. Chen ... “Modified magnetic equivalent circuit ...” ...
```

The second broken form is invalid because it dropped authors that are present in the authoritative source.

## Example

Input:

```text
Attention Is All You Need
```

Output shown in chat:

```text
[1] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, et al., “Attention is all you need,” in Proc. Adv. Neural Inf. Process. Syst. (NeurIPS), Long Beach, CA, USA, Dec. 2017, pp. 5998–6008.
```

Saved file:

```text
ieee_citations.docx
```

In the Word document, the paragraph should be justified, use Times New Roman, italicize the venue name, and superscript ordinal suffixes where present.

## Tools

- Use local file reads for input files and JSON data files.
- Use web search only to fill or verify missing citation metadata.
- Create an output `.docx` file when the user asks for one or provides a source citation file.
