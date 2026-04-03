# Test Cases

Manual test scenarios for verifying the IEEE Citation Generator skill.

## T1: Well-known paper by title only

**Input:** `Attention Is All You Need`

**Expected output shown in chat:**
```text
[1] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, et al., “Attention is all you need,” in Proc. Adv. Neural Inf. Process. Syst. (NeurIPS), Long Beach, CA, USA, 2017, pp. 5998–6008.
```

**Verify:**
- [x] All authors listed (6 + et al. since there are 8 authors)
- [x] Conference name abbreviated
- [x] City, state, country included
- [x] Saved `ieee_citations.docx` contains the citation as a Word paragraph
- [x] Title quotes and page-range punctuation are preserved correctly in Word output
- [x] The Word paragraph uses Times New Roman
- [x] The Word paragraph is justified
- [x] The conference venue name is italicized in Word output

## T2: Partial citation missing DOI

**Input:** `K. He, X. Zhang, S. Ren, J. Sun, Deep Residual Learning for Image Recognition, CVPR 2016`

**Expected output shown in chat:**
```text
[1] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image recognition,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Las Vegas, NV, USA, 2016, pp. 770–778, doi: 10.1109/CVPR.2016.90.
```

**Verify:**
- [x] DOI fetched via web search
- [x] "and" added before last author
- [x] Conference name fully abbreviated

## T3: Batch file with 3 citations

**Input:** File `input-batch.txt`

**Expected output:** 5 numbered citations, each properly formatted, saved to `input-batch_ieee.docx`

**Verify:**
- [x] Sequential numbering [1] through [5]
- [x] Each citation type handled correctly (conference, conference, journal/conference, website, book)
- [x] Output file created
- [x] The generated Word file contains one citation per paragraph
- [x] Every paragraph uses Times New Roman and justified alignment

## T4: Non-IEEE paper (ACM)

**Input:** `Attention is all you need`

**Expected output:** IEEE-style formatting (not ACM style), even though this was published at NeurIPS

**Verify:**
- [x] Uses IEEE citation format, not ACM
- [x] Conference name abbreviated per IEEE rules

## T5: Website citation

**Input:** `https://pytorch.org/docs/stable/index.html`

**Expected output shown in chat:**
```text
[1] “PyTorch documentation.” PyTorch. https://pytorch.org/docs/stable/index.html (accessed Mon. Day, Year).
```

**Verify:**
- [x] Page title extracted from URL or web fetch
- [x] Access date is today's date
- [x] URL is bare (no angle brackets)

## T6: Book citation

**Input:** `Deep Learning by Goodfellow, Bengio, and Courville`

**Expected output shown in chat:**
```text
[1] I. Goodfellow, Y. Bengio, and A. Courville, Deep Learning. Cambridge, MA, USA: MIT Press, 2016.
```

**Verify:**
- [x] Book title not in quotes
- [x] Publisher city, state/country, and publisher name
- [x] No edition listed (it's the first edition)

## T7: Paper with 8+ authors (et al.)

**Input:** `Language Models are Few-Shot Learners`

**Expected output shown in chat:**
```text
[1] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, et al., “Language models are few-shot learners,” in Proc. Adv. Neural Inf. Process. Syst. (NeurIPS), Virtual, 2020, pp. 1877–1901.
```

**Verify:**
- [x] First 6 authors listed, then "et al."
- [x] Not all 14 authors listed

## T8: Unknown journal - word-level abbreviation fallback

**Input:** `Some paper in Journal of Electrical Engineering and Technology`

**Expected output:** Journal abbreviated as `J. Elect. Eng. Technol.`

**Verify:**
- [x] Word-level rules applied: Journal->J., Electrical->Elect., Engineering->Eng., Technology->Technol.
- [x] "of" and "and" dropped

## T9: arXiv preprint

**Input:** `arXiv:2005.14165`

**Expected output shown in chat:**
```text
[1] T. Brown, B. Mann, N. Ryder, M. Subbiah, J. D. Kaplan, P. Dhariwal, et al., “Language models are few-shot learners,” arXiv preprint arXiv:2005.14165, 2020.
```

**Verify:**
- [x] arXiv ID preserved
- [x] No volume/page numbers
- [x] Authors still resolved

## T10: IEEE journal article with full metadata

**Input:** `Z. Yang et al., “Design of hairpin winding electric machines,” IEEE Trans. Transport. Electrific., vol. 9, no. 1, pp. 1200-1210, Mar. 2023`

**Expected output shown in chat:**
```text
[1] Z. Yang et al., “Design of hairpin winding electric machines,” IEEE Trans. Transport. Electrific., vol. 9, no. 1, pp. 1200–1210, Mar. 2023.
```

**Verify:**
- [x] Hyphen replaced with the intended page-range dash in the saved Word document
- [x] Already-abbreviated journal name preserved
- [x] Existing format mostly retained with minor fixes
- [x] The journal venue name is italicized in the Word document

## T11: Word output punctuation fidelity

**Input:** File `input-single.txt`

**Expected output:** `input-single_ieee.docx`

**Verify:**
- [x] The saved Word document contains one citation paragraph
- [x] Title quotes remain curly quotes in the saved document
- [x] Page ranges render with an en dash in Word output

## T12: Ordinal superscript formatting

**Input:** `Proceedings of the 24th International Conference on Electrical Machines and Systems`

**Expected output:** a `.docx` citation containing `24th` in the venue text

**Verify:**
- [x] The ordinal suffix `th` is superscripted in the Word document
- [x] The same superscript rule applies to `1st`, `2nd`, `3rd`, and edition ordinals such as `2nd ed.`

## T13: Three-author punctuation regression

**Input:** `M. Cheng, P. Han, Z. Wu, Editorial for the special issue on advanced electric machines and drives for battery, hybrid, and fuel cell electric vehicles, Chinese Journal of Electrical Engineering, vol. 7, no. 3, pp. 1-3, Sep. 2021`

**Expected output shown in chat:**
```text
[1] M. Cheng, P. Han and Z. Wu, “Editorial for the special issue on advanced electric machines and drives for battery, hybrid, and fuel cell electric vehicles,” Chin. J. Elect. Eng., vol. 7, no. 3, pp. 1–3, Sep. 2021.
```

**Verify:**
- [x] No Oxford comma before `and` for exactly 3 authors
- [x] Curly quotes preserved around the title
- [x] Hyphen replaced with en dash in the page range

## T14: Four-author punctuation rule

**Input:** `A. Smith, B. Jones, C. Lee, D. Brown, Sample conference paper, ICCV 2023`

**Expected output:** Uses an Oxford comma before `and` in the four-author list.

**Verify:**
- [x] Four-author output uses `A. Smith, B. Jones, C. Lee, and D. Brown`
- [x] Title uses curly quotes

## T15: Two-author punctuation rule

**Input:** `A. Smith, B. Jones, Sample journal article, IEEE Transactions on Power Electronics, vol. 1, no. 2, pp. 10-20, Jan. 2024`

**Expected output:** Uses `A. Smith and B. Jones` with no comma before `and`.

**Verify:**
- [x] Two-author output omits the comma before `and`
- [x] Page range uses an en dash
