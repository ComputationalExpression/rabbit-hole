"""Down the Rabbit Hole.

CMPSC 100: Computational Expression, Activity 8

Read a book from a text file, count its words in a dictionary, answer
questions about them, and write what you found to files. Start with Alice's
Adventures in Wonderland, then analyze a book of your own from Project
Gutenberg.

Your program should work for any book, so take every number it reports from
the file itself rather than from a count made by hand.

Author: TODO
"""

# Change BOOK to the file name of your own book once the checks pass, and
# HEADING to the first word of each chapter heading in it
BOOK = "alice.txt"
HEADING = "CHAPTER"
REPORT = "report.txt"
SEARCHES = "searches.txt"

# The characters stripped from both ends of a word, so that "Alice," and
# "_Alice_" both count as "alice". Project Gutenberg books also use curly
# quotes and long dashes, and many begin with an invisible marker, "\ufeff"
PUNCTUATION = ".,;:!?\"'()[]*_-\u201c\u201d\u2018\u2019\u2014\ufeff"


def main():
    print("=" * 50)
    print("DOWN THE RABBIT HOLE")
    print("=" * 50)

    # TODO 1: ask three questions, in this order, and save each answer to the
    # variable named here
    # `name`: the user's name
    # `search`: which word to look up, made lower case with .lower()
    # `least`: how many letters at least (an int)

    # TODO 2: set `lines`, `chapters` and `words` to 0, and `counts` to an
    # empty dictionary

    # TODO 3: open BOOK with encoding="utf-8" and loop over its lines. On
    # every trip/iteration:
    # add 1 to `lines`
    # split the line into a list of its words with
    # line.replace("—", " ").split(). The replace turns each long dash into
    # a space first, because a book can join two words with one
    # if that list is not empty and its first item is HEADING, add 1 to
    # `chapters`
    # then loop over the list. Make each word lower case and strip
    # PUNCTUATION from it. If what is left is not "", add 1 to `words`, and
    # add 1 to its count in `counts`, or give it a count of 1 if it is not a
    # key yet

    # TODO 4: save the count of `search` to `times`, or 0 if it is not a key

    # TODO 5: set `common` to "none", `most` to 0, and `longest` to "". Then
    # loop over the keys of `counts`. On every trip/iteration:
    # if the word has at least `least` letters and its count is more than
    # `most`, save the word to `common` and its count to `most`
    # if the word is longer than `longest`, save it to `longest`

    # TODO 6: make a list named `results` of eight strings, each a label
    # followed by its value:
    # Lines: `lines`
    # Chapters: `chapters`
    # Words: `words`
    # Different words: the number of keys in `counts`
    # Times: `times`
    # Most common: `common`
    # Count: `most`
    # Longest: `longest`

    # TODO 7: open REPORT with "w" and write each string of `results` to it,
    # one per line. Then open SEARCHES with "a" and write one line: `search`,
    # a colon and a space, and `times`

    # TODO 8: print a blank line, a line of 50 "=", "BOOK LOG:" followed by
    # the name, and another line of 50 "=". Then print each string of
    # `results`


if __name__ == "__main__":
    main()
