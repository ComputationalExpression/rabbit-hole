# Activity 8: Down the Rabbit Hole

|Item |       |
|:----|:------|
|Released |Monday, November 2, in class |
|Due |Wednesday, November 4, 9:00am |
|Progress |[![Grade](../../actions/workflows/main.yml/badge.svg?branch=main)](../../actions/workflows/main.yml) |

Your program reads a book, counts its words in a dictionary, looks one up, and writes what it
found to two files. You build it on `alice.txt`, Lewis Carroll's *Alice's
Adventures in Wonderland*, then download a book you like from Project Gutenberg and analyze that
one. If a step confuses you, please ask about it while you are still in the room.

## Course learning outcomes

This activity addresses the following course learning outcomes:

**CLO 1.** Apply Python programming fundamentals to execute and explain computer code that
implements interactive, novel solutions to a variety of computable problems.

**CLO 2.** Implement code consistent with industry-standard practices using professional-grade
integrated development environments (IDEs), command-line tools, and version control systems.

Specifically, by the end of this activity you should be able to:

* download a text file and read it line by line with `encoding="utf-8"`
* count words in a dictionary, and look one up after checking it is a key
* write a file with `"w"` and add to a file with `"a"`

## The problem

The questions, the log, and two helper functions are provided in `src/main.py`:
`words_in(line)` returns the words of a line in lower case without punctuation, and
`most_common(counts, least)` returns the word with the highest count among words with at least
`least` letters. You write four steps:

1. Read `BOOK` line by line and count every word in the dictionary `counts`
2. Look up the word typed in, so `Times` is its count, or `0` when it is not a key
3. Write the results to `report.txt` with `"w"`, so each run replaces it
4. Add one line to `searches.txt` with `"a"`, so each run adds to its end: the word and its
   count, such as `rabbit: 43`

### Example run

```text
$ uv run python src/main.py
==================================================
DOWN THE RABBIT HOLE
==================================================
What is your name? JJ
Which word should I look up? Rabbit
How many letters at least? 7

==================================================
BOOK LOG: JJ
==================================================
Words: 26552
Different words: 2664
Times: 43
Most common: herself
Count: 83
```

## Getting started

Open `src/main.py` and work through the `TODO` markers in order. Run it as you go, rather than
writing all of it and running it once:

```text
uv run python src/main.py
```

Put your name on the `Author:` line at the top of the file, and delete each `TODO` marker as
you finish that step.

## Your own book

Once the checks pass on `alice.txt`, analyze a book you choose:

1. Find a book on [Project Gutenberg](https://www.gutenberg.org/), which holds over 75,000 free
   books whose copyright has expired
2. On the book's page, find the download formats, right-click **Plain Text**, and save the
   linked file into the top folder of this repository, with a short name and no spaces, such as
   `frankenstein.txt`
3. Open the file in VS Code. Delete every line up to and including the one that starts with
   `*** START OF`, and every line from the one that starts with `*** END OF` to the end of the
   file. Those lines are Project Gutenberg's notes and license, not the book
4. In `src/main.py`, set `BOOK` to the file name
5. Run the program and look up a few words: a character's name, a place, a word the book is about

The checks still run on `alice.txt` and the short book of their own, so they pass with your book
in `BOOK`.

## Evaluation

In-class activities are graded on completion and contribute to the **In-Class Activities**
category on the syllabus (10 points, averaged across the semester). This activity is worth one
activity grade. What is graded is the attempt, not whether every value comes out right.

|Level |What it looks like |
|:-----|:------------------|
|**Complete** |At least half of the activity is done |
|**Partial** |Less than half is done, but something beyond the starter was committed |
|**Incomplete** |Nothing was changed |

Run the automated checks yourself, as many times as you like, from the top folder of this
repository rather than from inside `src`:

```text
uv run gatorgrade --config gatorgrade.yml
```

Each check's description says what to look at when it fails. Under a failed check, gatorgrade
also prints a `uv run pytest ...` command. Run it: the last lines name the line that came out
wrong, what it said, what was expected, and the book that was used.

> [!NOTE]
> Automated results are preliminary. Your instructor sets the final grade.

## Submitting

Commit and push often. The last version pushed before the deadline is the one that gets
graded. Commit your book's file, and the `report.txt` and `searches.txt` from runs on it. Use
your book's file name in place of `frankenstein.txt` below.

**In the terminal:**

```text
git add src/main.py frankenstein.txt report.txt searches.txt
git commit -m "Complete the rabbit hole activity"
git push
```

**In VS Code**, the Source Control panel in the left sidebar does the same three steps:

1. Click **+** next to a changed file to stage it, which is `git add`
2. Type a message in the box at the top, then click the checkmark, which is `git commit`
3. Click **Sync Changes** (or the up arrow) to push

Either way, then open your repository on GitHub and confirm your latest changes are actually
there.

If you need more time, apply a late token with [this form](https://forms.gle/3nGbpaNrG96DpLLdA).
