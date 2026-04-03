# Test Cases

Manual test scenarios for verifying the IEEE Citation Generator skill.

## T1: Well-known paper by title only

**Input:** `Attention Is All You Need`

**Expected output shown in chat:**

```text
[1] A. Vaswani, N. Shazeer, N. Parmar, J. Uszkoreit, L. Jones, A. N. Gomez, et al., “Attention is all you need,” in Proc. Adv. Neural Inf. Process. Syst. (NeurIPS), Long Beach, CA, USA, Dec. 2017, pp. 5998–6008.
```

**Verify:**

- [x] All authors listed correctly
- [x] Conference name abbreviated
- [x] City, state, country included
- [x] Saved `ieee_citations.docx` contains the citation as a Word paragraph
- [x] Title quotes and page-range punctuation are preserved correctly in Word output
- [x] The Word paragraph uses Times New Roman
- [x] The Word paragraph is justified
- [x] The conference venue name is italicized in Word output

## T2: Partial citation missing metadata

**Input:** `K. He, X. Zhang, S. Ren, J. Sun, Deep Residual Learning for Image Recognition, CVPR 2016`

**Expected output shown in chat:**

```text
[1] K. He, X. Zhang, S. Ren, and J. Sun, “Deep residual learning for image recognition,” in Proc. IEEE Conf. Comput. Vis. Pattern Recognit. (CVPR), Las Vegas, NV, USA, Jun. 2016, pp. 770–778.
```

**Verify:**

- [x] Missing metadata is fetched from authoritative sources
- [x] The author list is rebuilt in IEEE form
- [x] Conference name is abbreviated correctly

## T3: Batch file

**Input:** File `input-batch.txt`

**Expected output:** 5 numbered citations, each properly formatted, saved to `input-batch_ieee.docx`

**Verify:**

- [x] Sequential numbering `[1]` through `[5]`
- [x] Each citation type handled correctly
- [x] Output file created
- [x] The generated Word file contains one citation per paragraph
- [x] Every paragraph uses Times New Roman and justified alignment

## T4: Website citation

**Input:** `https://pytorch.org/docs/stable/index.html`

**Expected output shown in chat:**

```text
[1] “PyTorch documentation.” PyTorch. https://pytorch.org/docs/stable/index.html (accessed Mon. Day, Year).
```

**Verify:**

- [x] Page title extracted from the page
- [x] Access date is current
- [x] URL is bare

## T5: Three-author punctuation regression

**Input:** `M. Cheng, P. Han, Z. Wu, Editorial for the special issue on advanced electric machines and drives for battery, hybrid, and fuel cell electric vehicles, Chinese Journal of Electrical Engineering, vol. 7, no. 3, pp. 1-3, Sep. 2021`

**Expected output shown in chat:**

```text
[1] M. Cheng, P. Han and Z. Wu, “Editorial for the special issue on advanced electric machines and drives for battery, hybrid, and fuel cell electric vehicles,” Chin. J. Elect. Eng., vol. 7, no. 3, pp. 1–3, Sep. 2021.
```

**Verify:**

- [x] No Oxford comma before `and` for exactly 3 authors
- [x] Curly quotes are preserved around the title
- [x] Hyphen is replaced with an en dash in the page range

## T6: Reported regression - punctuation corruption in Ref. 15

**Input:**

```text
[15] R. Wang, S. Pekarek, P. O'Regan, A. Larson, and R. van Maaren, ?Incorporating skew in a magnetic equivalent circuit model of synchronous machines,? IEEE Trans. Energy Convers., vol. 30, no. 2, pp. 816?818, Jun. 2015.
```

**Expected output shown in chat:**

```text
[15] R. Wang, S. Pekarek, P. O'Regan, A. Larson, and R. van Maaren, “Incorporating skew in a magnetic equivalent circuit model of synchronous machines,” IEEE Trans. Energy Convers., vol. 30, no. 2, pp. 816–818, Jun. 2015.
```

**Verify:**

- [x] Opening and closing title quotes are normalized from `?` to `“` and `”`
- [x] Page-range dash is normalized from `?` to `–`
- [x] No stray `?` characters remain in the final citation

## T7: Reported regression - missing authors in Ref. 16

**Input:**

```text
[16] J. Chen, W. Hua, L. Shao, and Z. Wu, ?Modified magnetic equivalent circuit of double-stator single-rotor axial flux permanent magnet machine considering stator radial-end flux-leakage,? IET Elect. Power Appl., vol. 18, no. 2, pp. 195?207, 2024.
```

**Expected output shown in chat:**

```text
[16] J. Chen, W. Hua, L. Shao and Z. Wu, “Modified magnetic equivalent circuit of double-stator single-rotor axial flux permanent magnet machine considering stator radial-end flux-leakage,” IET Elect. Power Appl., vol. 18, no. 2, pp. 195–207, 2024.
```

**Verify:**

- [x] All authors from the authoritative source are preserved
- [x] The title punctuation is normalized
- [x] The page range uses an en dash
- [x] The final citation does not collapse the author list to a single leading author

## T8: Word output punctuation fidelity

**Input:** File `input-single.txt`

**Expected output:** `input-single_ieee.docx`

**Verify:**

- [x] The saved Word document contains one citation paragraph
- [x] Title quotes remain curly quotation marks in the saved document
- [x] Page ranges render with en dashes in Word output

## T9: Ordinal superscript formatting

**Input:** `Proceedings of the 24th International Conference on Electrical Machines and Systems`

**Expected output:** a `.docx` citation containing `24th` in the venue text

**Verify:**

- [x] The ordinal suffix `th` is superscripted in the Word document
- [x] The same superscript rule applies to `1st`, `2nd`, `3rd`, and edition ordinals such as `2nd ed.`
