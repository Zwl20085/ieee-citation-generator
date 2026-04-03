---
name: "ieee-citation-generator"
description: "Use when the user asks for IEEE-formatted citations from paper titles, rough citation text, URLs, or a plain-text file of references. Resolve missing metadata, abbreviate venues with IEEE-style rules, and save the formatted references to a Word document."
---

# IEEE Citation Generator

Generate properly formatted IEEE references from paper titles, partial citations, URLs, or plain-text citation files.

## Trigger

Use this skill when the user asks for IEEE citations, mentions `ieee-citation-generator`, or wants citations reformatted into IEEE style.

## Inputs

- Direct text: one title, one citation, or several entries separated by blank lines or numbering
- File path: a readable plain-text citation file containing one citation per non-empty line

## Workflow

1. Parse the input.
   - If the input looks like a readable plain-text file path, read that file and treat each non-empty line as one entry.
   - Otherwise, treat the input as direct citation text.
2. Classify each entry.
   - Title only: perform a web lookup for full metadata.
   - Partial citation: fill in missing fields with targeted web lookup.
   - Full citation in another style: reformat into IEEE.
   - Already IEEE-like: verify and correct.
3. Resolve missing metadata carefully.
   - Search the exact title first.
   - If needed, search title plus an author name.
   - Use DOI or arXiv pages directly when available.
   - Verify the result matches the intended work before formatting.
4. After generating each reference, run a final verification pass.
   - Re-check the author list and author-name order against the best available source.
   - Confirm the publication date is complete and correctly reflected in the citation.
   - Check whether any information was lost during formatting, such as missing authors, pages, article numbers, venue details, city/country, month, or year.
   - If the web result is incomplete or conflicting, continue searching until the citation is as complete and accurate as the available sources allow, or surface the ambiguity to the user.
5. Load the local data files from this skill directory before formatting:
   - `data/journal-abbreviations.json`
   - `data/conference-abbreviations.json`
   - `data/publisher-templates.json`
6. Apply IEEE formatting rules.
7. Return the final references numbered as `[1]`, `[2]`, and so on in the chat response.
8. When the user provided a file or asked for an output file, save the results to:
   - `<input_basename>_ieee.docx` next to the source file, or
   - `ieee_citations.docx` in the current working directory for direct text
9. Create the saved `.docx` with one justified paragraph per reference, using Times New Roman, italic journal and conference venue names, curly quotes around titles, en dashes for page ranges, and superscript ordinal suffixes such as `st`, `nd`, `rd`, and `th`.

## Required Metadata

| Type | Required fields |
|---|---|
| Journal | Authors, title, journal name, volume, issue if available, pages or article number, month, year |
| Conference | Authors, title, conference name, city, country, month, year, pages if available |
| Book | Authors or editors, title, edition if not first, city, country, publisher, year |
| Website | Author if available, page title, site name, URL, access date |

## Abbreviation Rules

### Journals

1. Check `journal-abbreviations.json` for an exact venue match.
2. If not found, fall back to word-level abbreviation rules from `conference-abbreviations.json`.
3. If still uncertain, use standard IEEE or ISO 4 abbreviation style.

### Conferences

1. Check `conference-abbreviations.json` under `full_conference_names`.
2. Otherwise abbreviate word by word using `word_abbreviations`.
3. Keep proper nouns and acronyms. Drop articles when appropriate.

## Formatting Rules

Return citations as plain text in chat. Save the canonical deliverable as a `.docx` file.

Apply these punctuation rules everywhere: instructions, examples, chat output, and the saved `.docx`.

The saved Word document should format citations as:
- Times New Roman for all citation text
- fully justified paragraph alignment
- one citation paragraph per reference
- curly quotation marks `“ ”` around article and paper titles, never straight ASCII `"` quotes
- en dash `–` for page ranges, never hyphen `-`
- italic journal and conference venue names only
- superscript ordinal suffixes such as `st`, `nd`, `rd`, and `th` wherever they appear

### Journal article

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

### Conference paper

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

### Book

```text
[N] A. B. Surname, Title of Book, Xth ed. City, Country: Publisher, Year.
```

Rules:
- Superscript ordinal suffixes such as `2nd ed.` or `3rd ed.` in the Word document.

### Book chapter

```text
[N] A. B. Surname, “Chapter title,” in Title of Book, A. B. Editor, Ed. City, Country: Publisher, Year, pp. Z1–Z2.
```

### Website

```text
[N] A. B. Surname. “Page title.” Website Name. URL (accessed Mon. Day, Year).
```

### arXiv preprint

```text
[N] A. B. Surname and C. D. Surname, “Title,” arXiv preprint arXiv:XXXX.XXXXX, Year.
```

## Special Handling

- All sources should be rendered in IEEE style regardless of original publisher.
- Use `publisher-templates.json` for publisher-specific quirks such as article numbers or series formatting.
- If a title maps to multiple possible works, surface the ambiguity and ask the user to choose.
- Preserve input order when formatting multiple entries.
- Treat author completeness, author-name order, publication date completeness, and dropped metadata as mandatory final checks before returning or saving the citations.

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
