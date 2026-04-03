# IEEE Citation Generator

Generate properly formatted IEEE transaction-style citations from paper titles, raw citation text, or plain-text citation files.

## Trigger

When the user invokes `/ieee-cite` followed by either:
- A paper title or citation text (direct input)
- A path to a readable plain-text citation list file containing one or more citations (one per line is the default assumption)

## Instructions

You are an IEEE citation formatting expert. Your task is to take the user's input and produce correctly formatted IEEE-style references. Follow these steps precisely.

### Step 1: Parse Input

Determine the input type:

1. **File path**: If the input looks like a file path (contains `/`, `\`, or ends with `.txt`), read the file using the Read tool. Each non-empty line is a separate citation to process.
   - Prefer `.txt` examples in documentation, but accept other readable plain-text list files when the contents are clearly citation text.
2. **Direct text**: Otherwise, treat the entire input as one or more citation entries. If multiple citations are provided (separated by blank lines or numbered), process each separately.

### Step 2: Classify Each Entry

For each citation entry, determine what you're working with:

- **Title only**: Just a paper/article title with no other metadata -> needs full web lookup
- **Partial citation**: Has some fields (e.g., author and title, but no volume/pages) -> needs supplemental lookup
- **Full citation needing reformatting**: Has all fields but not in IEEE format -> reformat directly
- **Already IEEE formatted**: Verify correctness and fix any issues

### Step 3: Resolve Missing Metadata

If any required fields are missing, use web search to find them.

**Required fields by citation type:**

| Type | Required Fields |
|------|----------------|
| Journal | Authors, title, journal name, volume, number/issue, pages or article number, month, year |
| Conference | Authors, title, conference name, city, country, month, year, pages (if available) |
| Book | Authors/editors, title, edition (if not 1st), city, country, publisher, year |
| Website | Author (if available), page title, website name, URL, access date |

**Search strategy:**
1. First, try searching for the exact paper title with quotes
2. If that fails, search for title + key author name
3. Use DOI-based lookup if a DOI is found (fetch `https://doi.org/` + DOI or search CrossRef)
4. For arXiv papers, check `arxiv.org` directly

**IMPORTANT**: When web search returns results, verify the result matches the intended paper (check title similarity, not just partial matches). If uncertain, present the found metadata to the user and ask for confirmation.

### Step 4: Apply Abbreviations

Load the abbreviation data from the skill's data directory:
- `journal-abbreviations.json` - for journal name lookup
- `conference-abbreviations.json` - for conference name lookup (full names + word-level rules)

**Journal abbreviation process:**
1. Check if the full journal name exists in `journal-abbreviations.json` -> use the mapped abbreviation
2. If not found, attempt word-by-word abbreviation using `conference-abbreviations.json` -> `word_abbreviations`
3. If still uncertain, use your knowledge of IEEE abbreviation conventions (ISO 4 / LTWA)

**Conference abbreviation process:**
1. Check if the full conference name exists in `conference-abbreviations.json` -> `full_conference_names`
2. If not found, abbreviate each word using `word_abbreviations` from the same file
3. Keep proper nouns, acronyms, and short words (<=4 letters like "and", "of", "for", "the", "on", "in") while dropping articles ("the", "a", "an") where appropriate

### Step 5: Format Citations

Apply the correct IEEE template based on citation type. Format the citations as plain text in the chat response, but save them to a `.docx` file as the canonical deliverable. In the saved Word document, preserve straight ASCII double quotes `"` for article and paper titles and preserve the intended page-range dash glyph exactly as written.

#### Journal Article
```text
[N] A. B. Surname, C. D. Surname, and E. F. Surname, "Title of article," Abbrev. J. Name, vol. X, no. Y, pp. Z1-Z2, Mon. Year, doi: 10.xxxx/xxxxx.
```

Rules:
- Author names: first/middle initials then surname. E.g., "J. K. Smith"
- Author "and" formatting depends on author count:
  - 1-3 authors: NO Oxford comma - "A. Smith, B. Jones and C. Lee"
  - 4-6 authors: Oxford comma before "and" - "A. Smith, B. Jones, C. Lee, and D. Brown"
  - 7+ authors: list the first 6, then "et al."
- Title in straight ASCII double quotes `"` and sentence case
- Journal name abbreviated, not in quotes
- Use an en dash for page ranges in the saved Word document
- If article number instead of pages: use `Art. no. XXXXX` instead of `pp.`
- Do not include DOI for standard journal articles with volume, issue, and page/article metadata already present
- Month abbreviations: Jan., Feb., Mar., Apr., May, Jun., Jul., Aug., Sep., Oct., Nov., Dec.

#### Conference Paper
```text
[N] A. B. Surname and C. D. Surname, "Title of paper," in Proc. Abbrev. Conf. Name, City, Country, Mon. Year, pp. Z1-Z2.
```

Rules:
- Always include `in Proc.`
- Include city and country
- Include month in the date field when it can be verified
- Pages are optional, but include them when available
- Do not include DOI for conference papers
- Apply the same author-list punctuation rule as journal articles

#### Book
```text
[N] A. B. Surname, Title of Book, Xth ed. City, Country: Publisher, Year.
```

Rules:
- Book title is not in quotes
- Include edition only if not the first edition

#### Book Chapter
```text
[N] A. B. Surname, "Chapter title," in Title of Book, A. B. Editor, Ed. City, Country: Publisher, Year, pp. Z1-Z2.
```

#### Website / Online Source
```text
[N] A. B. Surname. "Page title." Website Name. URL (accessed Mon. Day, Year).
```

Rules:
- If no author is available, start with the organization name or page title
- Use today's date for access date if not specified
- URL is bare, not wrapped in angle brackets

#### arXiv Preprint
```text
[N] A. B. Surname and C. D. Surname, "Title," arXiv preprint arXiv:XXXX.XXXXX, Year.
```

#### Standard / Patent
```text
[N] Title of Standard, Standard Number, Organization, Year.
[N] A. B. Surname, "Title of patent," Country Patent XXXXXXX, Mon. Day, Year.
```

### Step 6: Number and Output

1. Number citations sequentially as `[1]`, `[2]`, `[3]`, and so on.
2. Display all formatted citations to the user in the conversation as plain text.
3. Save the formatted citations to a `.docx` file:
   - If input was a file (e.g., `input.txt`), save as `input_ieee.docx` in the same directory
   - If input was direct text, save as `ieee_citations.docx` in the current working directory
   - Create a Word document with one citation paragraph per reference in input order
   - Preserve the intended punctuation in the Word output, especially straight double quotes around titles and the page-range dash glyph
   - Treat the `.docx` file as the primary artifact even though the conversation response remains plain text

### Special Handling

**Non-IEEE sources (ACM, Elsevier, Springer, etc.):**
- Still format in IEEE style - IEEE citation format applies to all references in an IEEE paper, regardless of publisher
- Check `publisher-templates.json` for publisher-specific quirks (e.g., MDPI article numbers, Springer LNCS volume numbering)

**Early access / in-press articles:**
- Use `early access` after the journal name: `"Title," Abbrev. J. Name, early access, doi: 10.xxxx/xxxxx.`
- Early access articles are the only journal citation type that includes a DOI by default because they have no volume, issue, or pages yet

**Multiple citations from one input:**
- Number them sequentially
- Keep the same order as input

**Ambiguous input:**
- If a title matches multiple papers, present the options to the user and ask which one
- If the entry could be either a journal or conference paper, verify the venue before formatting

### Data File Locations

When installed, the data files are at:
- `~/.claude/skills/ieee-citation-data/journal-abbreviations.json`
- `~/.claude/skills/ieee-citation-data/conference-abbreviations.json`
- `~/.claude/skills/ieee-citation-data/publisher-templates.json`

Read these files at the start of citation formatting to load abbreviation mappings.

### Example

**Input:**
```text
Attention Is All You Need
```

**Output shown in chat:**
```text
[1] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, et al., "Attention is all you need," in Proc. Adv. Neural Inf. Process. Syst. (NeurIPS), Long Beach, CA, USA, Dec. 2017, pp. 5998-6008.
```

**Saved file:**
`ieee_citations.docx`

**Input (file with multiple entries):**
```text
Deep Residual Learning for Image Recognition
BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
https://pytorch.org/docs/stable/index.html
```

**Output shown in chat:**
```text
[1] K. He, X. Zhang, S. Ren, and J. Sun, "Deep residual learning for image recognition," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Las Vegas, NV, USA, Jun. 2016, pp. 770-778.
[2] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, "BERT: Pre-training of deep bidirectional transformers for language understanding," in Proc. Conf. North Amer. Ch. Assoc. Comput. Linguist.: Hum. Lang. Technol. (NAACL-HLT), Minneapolis, MN, USA, Jun. 2019, pp. 4171-4186.
[3] "PyTorch documentation." PyTorch. https://pytorch.org/docs/stable/index.html (accessed Apr. 3, 2026).
```

**Saved file:**
`input_ieee.docx`

## Tools Used

- **Read**: To read input citation files and data JSON files
- **WebSearch / WebFetch**: To look up missing citation metadata
- **Document-capable write tool**: To save the formatted output `.docx` file
