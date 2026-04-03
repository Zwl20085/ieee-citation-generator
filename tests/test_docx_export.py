from pathlib import Path

import pytest

docx = pytest.importorskip("docx")
Document = docx.Document

from scripts.export_ieee_docx import export_docx


def test_export_docx_applies_italics_and_superscript(tmp_path: Path):
    source = tmp_path / "input.txt"
    source.write_text(
        "\n".join(
            [
                '[1] A. B. Author, \u201cJournal paper,\u201d IEEE Trans. Magn., vol. 57, no. 7, pp. 1\u201312, Jul. 2021.',
                '[2] A. B. Author, \u201cConference paper,\u201d in Proc. 24th Int. Conf. Elect. Mach. Syst. (ICEMS), Gyeongju, South Korea, 2021, pp. 1\u20134.',
            ]
        ),
        encoding="utf-8",
    )
    output = tmp_path / "output.docx"

    export_docx(source, output)

    doc = Document(output)
    paragraphs = [p for p in doc.paragraphs if p.text.strip()]
    assert len(paragraphs) == 2

    journal_runs = [run for run in paragraphs[0].runs if run.text]
    conference_runs = [run for run in paragraphs[1].runs if run.text]

    assert any("IEEE Trans. Magn." in run.text and run.italic for run in journal_runs)
    assert any(run.text == "24" and run.italic and not run.font.superscript for run in conference_runs)
    assert any(run.text == "th" and run.italic and run.font.superscript for run in conference_runs)
    assert any("Int. Conf. Elect. Mach. Syst. (ICEMS)" in run.text and run.italic for run in conference_runs)


def test_export_docx_normalizes_tabs_into_single_spaces(tmp_path: Path):
    source = tmp_path / "input.txt"
    source.write_text(
        '[1]\tA. B. Author,\t\u201cTitle,\u201d\tIEEE Trans. Magn., vol. 57, no. 7, pp. 1\u201312, Jul. 2021.\n',
        encoding="utf-8",
    )
    output = tmp_path / "output.docx"

    export_docx(source, output)

    doc = Document(output)
    paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
    assert paragraphs == ['[1] A. B. Author, “Title,” IEEE Trans. Magn., vol. 57, no. 7, pp. 1–12, Jul. 2021.']
