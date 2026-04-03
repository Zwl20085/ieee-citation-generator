from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

CLAUDE_SKILL = REPO_ROOT / "skills" / "ieee-citation-generator.md"
CODEX_SKILL = REPO_ROOT / "codex" / "ieee-citation-generator" / "SKILL.md"
README = REPO_ROOT / "README.md"
INSTALLATION = REPO_ROOT / "installation.md"
TEST_CASES = REPO_ROOT / "tests" / "test-cases.md"

REPO_DOCS = [CLAUDE_SKILL, CODEX_SKILL, README, INSTALLATION, TEST_CASES]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_repo_docs_are_free_of_known_mojibake_sequences():
    bad_tokens = ["鈥", "揱", "漙", "锟", "�"]

    for path in REPO_DOCS:
        text = read_text(path)
        for token in bad_tokens:
            assert token not in text, f"{path} still contains mojibake token {token!r}"


def test_skill_docs_require_punctuation_normalization_and_author_restoration():
    for path in [CLAUDE_SKILL, CODEX_SKILL]:
        text = read_text(path)
        assert "Never keep a shortened or truncated input author list" in text
        assert "placeholder `?` characters in the final citation" in text
        assert "“Incorporating skew in a magnetic equivalent circuit model of synchronous machines,”" in text
        assert "J. Chen, W. Hua, L. Shao and Z. Wu" in text


def test_supporting_docs_explain_corruption_and_word_output_requirements():
    readme = read_text(README)
    installation = read_text(INSTALLATION)

    assert "Never substitute `?` for quotation marks or page-range dashes" in readme
    assert "Output shows `?` instead of quotes or page dashes" in installation
    assert "Replace the affected characters with curly quotes `“ ”` and en dashes `–`" in installation


def test_manual_tests_include_the_two_reported_regressions():
    cases = read_text(TEST_CASES)

    assert "T6: Reported regression - punctuation corruption in Ref. 15" in cases
    assert "T7: Reported regression - missing authors in Ref. 16" in cases
    assert "pp. 816–818" in cases
    assert "J. Chen, W. Hua, L. Shao and Z. Wu" in cases
