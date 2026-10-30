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


def test_words_are_counted_in_a_dictionary():
    assert "r" in modes(), "found no open(BOOK): read the book with `with open(BOOK) as file:`"
    stores = [
        n for n in nodes(ast.Subscript)
        if isinstance(n.ctx, ast.Store) and isinstance(n.value, ast.Name)
    ]
    assert stores, "found no `counts[word] = ...`: each word's count is stored under the word as its key"
    checks = [
        n for n in nodes(ast.Compare)
        if any(isinstance(op, (ast.In, ast.NotIn)) for op in n.ops)
    ]
    assert checks, "found no `in` or `not in` check: test whether a word is a key before adding 1 to it"


def test_files_are_written_with_w_and_a():
    found = modes()
    assert "w" in found, 'found no open(REPORT, "w"): "w" starts the report over on every run'
    assert "a" in found, 'found no open(SEARCHES, "a"): "a" adds a line to the end on every run'
