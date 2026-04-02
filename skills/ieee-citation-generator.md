# IEEE Citation Generator

Generate properly formatted IEEE transaction-style citations from paper titles, raw citation text, or text files.

## Trigger

When the user invokes `/ieee-cite` followed by either:
- A paper title or citation text (direct input)
- A path to a `.txt` file containing one or more citations (one per line)

## Instructions

You are an IEEE citation formatting expert. Your task is to take the user's input and produce correctly formatted IEEE-style references. Follow these steps precisely.

### Step 1: Parse Input

Determine the input type:

1. **File path**: If the input looks like a file path (contains `/`, `\`, or ends with `.txt`), read the file using the Read tool. Each non-empty line is a separate citation to process.
2. **Direct text**: Otherwise, treat the entire input as one or more citation entries. If multiple citations are provided (separated by blank lines or numbered), process each separately.

### Step 2: Classify Each Entry

For each citation entry, determine what you're working with:

- **Title only**: Just a paper/article title with no other metadata → needs full web lookup
- **Partial citation**: Has some fields (e.g., author and title, but no volume/pages) → needs supplemental lookup
- **Full citation needing reformatting**: Has all fields but not in IEEE format → reformat directly
- **Already IEEE formatted**: Verify correctness and fix any issues

### Step 3: Resolve Missing Metadata

If any required fields are missing, use web search to find them.

**Required fields by citation type:**

| Type | Required Fields |
|------|----------------|
| Journal | Authors, title, journal name, volume, number/issue, pages or article number, month, year, DOI (if available) |
| Conference | Authors, title, conference name, city, country, year, pages (if available) |
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
- `journal-abbreviations.json` — for journal name lookup
- `conference-abbreviations.json` — for conference name lookup (full names + word-level rules)

**Journal abbreviation process:**
1. Check if the full journal name exists in `journal-abbreviations.json` → use the mapped abbreviation
2. If not found, attempt word-by-word abbreviation using `conference-abbreviations.json` → `word_abbreviations`
3. If still uncertain, use your knowledge of IEEE abbreviation conventions (ISO 4 / LTWA)

**Conference abbreviation process:**
1. Check if the full conference name exists in `conference-abbreviations.json` → `full_conference_names`
2. If not found, abbreviate each word using `word_abbreviations` from the same file
3. Keep proper nouns, acronyms, and short words (≤4 letters like "and", "of", "for", "the", "on", "in") — drop articles ("the", "a", "an") but keep prepositions

### Step 5: Format Citations

Apply the correct IEEE template based on citation type. Use plain text (no italics/bold markup since output is `.txt`).

#### Journal Article
```
[N] A. B. Surname, C. D. Surname, and E. F. Surname, "Title of article," Abbrev. J. Name, vol. X, no. Y, pp. Z1–Z2, Mon. Year, doi: 10.xxxx/xxxxx.
```

Rules:
- Author names: first/middle initials then surname. E.g., "J. K. Smith"
- Use "and" before the last author
- For 7+ authors: list first 6, then "et al."
- Title in double quotes, sentence case (capitalize first word and proper nouns only)
- Journal name abbreviated, NOT in quotes
- Use en-dash (–) for page ranges, not hyphen (-)
- If article number instead of pages: use "Art. no. XXXXX" instead of "pp."
- Include DOI if available, formatted as `doi: 10.xxxx/xxxxx.` (lowercase "doi", with period at end)
- Month abbreviated: Jan., Feb., Mar., Apr., May, Jun., Jul., Aug., Sep., Oct., Nov., Dec.

#### Conference Paper
```
[N] A. B. Surname and C. D. Surname, "Title of paper," in Proc. Abbrev. Conf. Name, City, Country, Year, pp. Z1–Z2.
```

Rules:
- "in Proc." before conference name (lowercase "in")
- Include city and country
- Pages optional (include if available)
- If DOI available, append: `doi: 10.xxxx/xxxxx.`

#### Book
```
[N] A. B. Surname, Title of Book, Xth ed. City, Country: Publisher, Year.
```

Rules:
- Book title is NOT in quotes (in print it would be italicized, but in plain text just write it directly)
- Include edition only if not the first edition ("2nd ed.", "3rd ed.", "4th ed.", etc.)
- Publisher city and country before publisher name, separated by colon

#### Book Chapter
```
[N] A. B. Surname, "Chapter title," in Title of Book, A. B. Editor, Ed. City, Country: Publisher, Year, pp. Z1–Z2.
```

#### Website / Online Source
```
[N] A. B. Surname. "Page title." Website Name. URL (accessed Mon. Day, Year).
```

Rules:
- If no author, start with the organization name or "Page title"
- Use today's date for access date if not specified
- URL is bare (no angle brackets)

#### arXiv Preprint
```
[N] A. B. Surname and C. D. Surname, "Title," arXiv preprint arXiv:XXXX.XXXXX, Year.
```

#### Standard / Patent
```
[N] Title of Standard, Standard Number, Organization, Year.
[N] A. B. Surname, "Title of patent," Country Patent XXXXXXX, Mon. Day, Year.
```

### Step 6: Number and Output

1. Number citations sequentially as [1], [2], [3], etc.
2. Display all formatted citations to the user in the conversation
3. Save the formatted citations to a `.txt` file:
   - If input was a file (e.g., `input.txt`), save as `input_ieee.txt` in the same directory
   - If input was direct text, save as `ieee_citations.txt` in the current working directory
   - Use the Write tool to create the output file

### Special Handling

**Non-IEEE sources (ACM, Elsevier, Springer, etc.):**
- Still format in IEEE style — IEEE citation format applies to ALL references in an IEEE paper, regardless of publisher
- Check `publisher-templates.json` for publisher-specific quirks (e.g., MDPI article numbers, Springer LNCS volume numbering)

**Early access / in-press articles:**
- Use "early access" after the journal name: `"Title," Abbrev. J. Name, early access, doi: 10.xxxx/xxxxx.`

**Multiple citations from one input:**
- Number them sequentially
- Keep the same order as input

**Ambiguous input:**
- If a title matches multiple papers, present the options to the user and ask which one
- If the entry could be either a journal or conference paper, check which venue it was published in

### Data File Locations

When installed, the data files are at:
- `~/.claude/skills/ieee-citation-data/journal-abbreviations.json`
- `~/.claude/skills/ieee-citation-data/conference-abbreviations.json`
- `~/.claude/skills/ieee-citation-data/publisher-templates.json`

Read these files at the start of citation formatting to load abbreviation mappings.

### Example

**Input:**
```
Attention Is All You Need
```

**Output:**
```
[1] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, et al., "Attention is all you need," in Proc. Adv. Neural Inf. Process. Syst. (NeurIPS), Long Beach, CA, USA, 2017, pp. 5998–6008.
```

**Input (file with multiple entries):**
```
Deep Residual Learning for Image Recognition
BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
https://pytorch.org/docs/stable/index.html
```

**Output:**
```
[1] K. He, X. Zhang, S. Ren, and J. Sun, "Deep residual learning for image recognition," in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Las Vegas, NV, USA, 2016, pp. 770–778, doi: 10.1109/CVPR.2016.90.
[2] J. Devlin, M.-W. Chang, K. Lee, and K. Toutanova, "BERT: Pre-training of deep bidirectional transformers for language understanding," in Proc. Conf. North Amer. Ch. Assoc. Comput. Linguist.: Hum. Lang. Technol. (NAACL-HLT), Minneapolis, MN, USA, 2019, pp. 4171–4186.
[3] "PyTorch documentation." PyTorch. https://pytorch.org/docs/stable/index.html (accessed Apr. 3, 2026).
```

## Tools Used

- **Read**: To read input `.txt` files and data JSON files
- **WebSearch / WebFetch**: To look up missing citation metadata
- **Write**: To save the formatted output `.txt` file
