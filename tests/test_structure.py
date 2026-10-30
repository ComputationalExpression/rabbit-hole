"""Structure checks for Activity 8: Down the Rabbit Hole.

These read `src/main.py` as Python, not as text, so the words in the TODO
comments do not count. Only real statements do.
"""

import ast
from pathlib import Path

SOURCE = Path(__file__).resolve().parent.parent / "src" / "main.py"


def tree():
    return ast.parse(SOURCE.read_text(encoding="utf-8"))


def nodes(kind):
    return [n for n in ast.walk(tree()) if isinstance(n, kind)]


def modes():
    """Return the mode given to every call to open, "r" when none is given."""
    found = []
    for call in nodes(ast.Call):
        if isinstance(call.func, ast.Name) and call.func.id == "open":
            mode = "r"
            if len(call.args) > 1 and isinstance(call.args[1], ast.Constant):
                mode = call.args[1].value
            found.append(mode)
    return found


def utf8_read():
    """Return True when some call to open for reading passes encoding="utf-8"."""
    for call in nodes(ast.Call):
        if isinstance(call.func, ast.Name) and call.func.id == "open" and len(call.args) < 2:
            for keyword in call.keywords:
                if keyword.arg == "encoding" and isinstance(keyword.value, ast.Constant):
                    if str(keyword.value.value).lower().replace("_", "-") in ("utf-8", "utf8", "utf-8-sig"):
                        return True
    return False


def test_words_are_counted_in_a_dictionary():
    assert "r" in modes(), "found no open(BOOK): read the book with `with open(BOOK, encoding=\"utf-8\") as file:`"
    assert utf8_read(), 'found no open(BOOK, encoding="utf-8"): a Project Gutenberg book is UTF-8, and without it Windows cannot read its curly quotes'

    stores = [
        n for n in nodes(ast.Subscript)
        if isinstance(n.ctx, ast.Store) and isinstance(n.value, ast.Name)
    ]
    assert stores, "found no `counts[word] = ...`: each word's count is stored under the word as its key"


def test_files_are_written_with_w_and_a():
    found = modes()
    assert "w" in found, 'found no open(REPORT, "w"): "w" starts the report over on every run'
    assert "a" in found, 'found no open(SEARCHES, "a"): "a" adds a line to the end on every run'
