"""Automated checks for Activity 8: Down the Rabbit Hole.

Every check reads the book log at the end of the run, never the lines
printed along the way, so the wording is yours. Log values are matched
loosely: any amount of whitespace, any letter case, and the colon is
optional, so `print("Words:", words)`, `print("Words: " + str(words))`
and `print(f"Words: {words}")` all read the same.

Most checks run your program on a short book written for the test as well as
on alice.txt, so a number counted by hand and typed in passes only for the
book it was counted from. Take every number from the file.

The report and searches files are written to a temporary folder during the
checks, so a run here never changes the files in your repository.

When a check fails, the assertion message says which line came out wrong,
what it said, what was expected, and the book that was used.
"""

import re
from pathlib import Path
from unittest.mock import patch

import main
from main import main as run_main

ALICE = Path(__file__).resolve().parent.parent / "alice.txt"

# Seven lines, two of them chapter headings. CHAPTER on line five is not the
# first word, so that line is not a heading, and "--" is not a word.
SHORT = """CHAPTER I.
The Cat and the Hat

"The cat," said the Hat, "is a CAT!"
a CHAPTER is not a headline
CHAPTER II.
-- _Cat_ -- cat.
"""


def run(capsys, tmp_path, book=None, search="cat", least=1, name="JJ"):
    """Run main() once on `book` (alice.txt when None) and return its output."""
    if book is None:
        path = ALICE
    else:
        path = tmp_path / "book.txt"
        path.write_text(book)
    original = main.BOOK, main.REPORT, main.SEARCHES
    main.BOOK = str(path)
    main.REPORT = str(tmp_path / "report.txt")
    main.SEARCHES = str(tmp_path / "searches.txt")
    try:
        with patch("builtins.input", side_effect=[name, search, str(least)]):
            run_main()
    finally:
        main.BOOK, main.REPORT, main.SEARCHES = original
    out, err = capsys.readouterr()
    assert err == "", "the program wrote to the error stream:\n" + err
    return out


def value(text, label, start=None):
    """Return the value printed after `label`, normalized, or None."""
    if start is not None:
        found = text.upper().find(start)
        if found < 0:
            return None
        text = text[found:]
    words = r"\s+".join(re.escape(word) for word in label.split())
    match = re.search(rf"^[ \t]*{words}[ \t]*:?[ \t]*([^\n]*)", text, re.IGNORECASE | re.MULTILINE)
    if match is None:
        return None
    return " ".join(match.group(1).split()).upper().rstrip(".! ")


def expect(capsys, tmp_path, label, want, book=None, **answers):
    """Run once and check that the book log line `label` says `want`."""
    out = run(capsys, tmp_path, book=book, **answers)
    which = "alice.txt" if book is None else "the short test book"
    context = f"{which}, looked up {answers.get('search', 'cat')!r}, at least {answers.get('least', 1)} letters"
    if "BOOK LOG" not in out.upper():
        raise AssertionError(f'no "BOOK LOG" line was printed ({context})')
    got = value(out, label, start="BOOK LOG")
    if got is None:
        raise AssertionError(f'no "{label}" line was printed after BOOK LOG ({context})')
    assert got == str(want).upper(), f'the "{label}" line said {got}, expected {want} ({context})'


def test_counts_lines_and_chapters(capsys, tmp_path):
    expect(capsys, tmp_path, "BOOK LOG", "JJ")
    expect(capsys, tmp_path, "Lines", 3356)
    expect(capsys, tmp_path, "Chapters", 12)
    # A blank line is still a line, and a heading has CHAPTER as its first word.
    expect(capsys, tmp_path, "Lines", 7, book=SHORT)
    expect(capsys, tmp_path, "Chapters", 2, book=SHORT)


def test_words_are_cleaned_and_counted(capsys, tmp_path):
    # "Cat", "cat," "CAT!" and "_Cat_" are all the word "cat", and "--" is no word.
    expect(capsys, tmp_path, "Words", 25, book=SHORT)
    expect(capsys, tmp_path, "Different words", 12, book=SHORT)
    expect(capsys, tmp_path, "Words", 26552)
    expect(capsys, tmp_path, "Different words", 2664)


def test_looks_up_a_word(capsys, tmp_path):
    expect(capsys, tmp_path, "Times", 5, book=SHORT, search="cat")
    expect(capsys, tmp_path, "Times", 2, book=SHORT, search="hat")
    # The word typed is made lower case before the lookup.
    expect(capsys, tmp_path, "Times", 5, book=SHORT, search="CAT")
    # A word that is not a key appears 0 times.
    expect(capsys, tmp_path, "Times", 0, book=SHORT, search="dog")
    expect(capsys, tmp_path, "Times", 386, search="alice")


def test_most_common_word_with_enough_letters(capsys, tmp_path):
    expect(capsys, tmp_path, "Most common", "cat", book=SHORT, least=1)
    expect(capsys, tmp_path, "Count", 5, book=SHORT, least=1)
    expect(capsys, tmp_path, "Most common", "chapter", book=SHORT, least=4)
    expect(capsys, tmp_path, "Count", 3, book=SHORT, least=4)
    # "chapter" has exactly 7 letters, which is at least 7.
    expect(capsys, tmp_path, "Most common", "chapter", book=SHORT, least=7)
    # No word is that long, so the answer is none and 0.
    expect(capsys, tmp_path, "Most common", "none", book=SHORT, least=9)
    expect(capsys, tmp_path, "Count", 0, book=SHORT, least=9)
    expect(capsys, tmp_path, "Most common", "alice", least=5)
    expect(capsys, tmp_path, "Most common", "caterpillar", least=10)
    expect(capsys, tmp_path, "Count", 27, least=10)


def test_longest_word(capsys, tmp_path):
    expect(capsys, tmp_path, "Longest", "headline", book=SHORT)
    expect(capsys, tmp_path, "Longest", "waistcoat-pocket")


def test_the_report_file_is_written_over(capsys, tmp_path):
    run(capsys, tmp_path, book=SHORT, search="cat")
    run(capsys, tmp_path, book=SHORT, search="dog")
    report = tmp_path / "report.txt"
    assert report.exists(), "no report file was written: open REPORT with \"w\" and write to it"
    text = report.read_text()
    for label, want in [("Lines", 7), ("Words", 25), ("Times", 0), ("Most common", "CAT"), ("Longest", "HEADLINE")]:
        got = value(text, label)
        assert got is not None, f'the report file has no "{label}" line'
        assert got == str(want), f'the report file\'s "{label}" line said {got}, expected {want}'
    # Two runs, and "w" starts the file over, so it holds one report.
    lines = len(re.findall(r"^[ \t]*Lines\b", text, re.IGNORECASE | re.MULTILINE))
    assert lines == 1, f"after two runs the report file has {lines} Lines lines, expected 1: open it with \"w\", not \"a\""


def test_the_searches_file_is_added_to(capsys, tmp_path):
    run(capsys, tmp_path, book=SHORT, search="cat")
    run(capsys, tmp_path, book=SHORT, search="dog")
    searches = tmp_path / "searches.txt"
    assert searches.exists(), "no searches file was written: open SEARCHES with \"a\" and write to it"
    text = searches.read_text()
    rows = [" ".join(line.split()).upper() for line in text.splitlines() if line.strip() != ""]
    assert len(rows) == 2, f"after two runs the searches file has {len(rows)} lines, expected 2: open it with \"a\", not \"w\""
    for row, want in zip(rows, ["CAT: 5", "DOG: 0"]):
        assert row.replace(" ", "") == want.replace(" ", ""), f"a searches line said {row}, expected {want}"
