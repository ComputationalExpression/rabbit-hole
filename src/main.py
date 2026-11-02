"""Down the Rabbit Hole.

CMPSC 100: Computational Expression, Activity 8

Read a book from a text file, count its words in a dictionary, look one up,
and write what you found to files. Start with Alice's Adventures in
Wonderland, then analyze a book of your own from Project Gutenberg.

Author: TODO
"""

# Change BOOK to the file name of your own book once the checks pass
BOOK = "alice.txt"
REPORT = "report.txt"
SEARCHES = "searches.txt"

# The characters stripped from both ends of a word, so that "Alice," and
# "_Alice_" both count as "alice". Project Gutenberg books also use curly
# quotes and long dashes, and many begin with an invisible marker, "﻿"
PUNCTUATION = ".,;:!?\"'()[]*_-“”‘’—﻿"


def words_in(line):
    """Return a list of the words of line, in lower case, without punctuation."""
    words = []
    # A long dash joins two words with no space, so it becomes a space first
    for part in line.replace("—", " ").split():
        word = part.lower().strip(PUNCTUATION)
        if word != "":
            words.append(word)
    return words


def most_common(counts, least):
    """Return the word with the highest count among words with at least least letters, or none."""
    best = "none"
    most = 0
    for word in counts:
        if len(word) >= least and counts[word] > most:
            best = word
            most = counts[word]
    return best


def main():
    print("=" * 50)
    print("DOWN THE RABBIT HOLE")
    print("=" * 50)

    name = input("What is your name? ")
    search = input("Which word should I look up? ").lower()
    least = int(input("How many letters at least? "))

    words = 0
    counts = {}
    # TODO 1: open BOOK with encoding="utf-8" and loop over its lines. For
    # each word in words_in(line), add 1 to `words`, and add 1 to the word's
    # count in `counts`, or give it a count of 1 if it is not a key yet

    times = 0
    # TODO 2: if `search` is a key of `counts`, save its count to `times`

    common = most_common(counts, least)
    most = 0
    if common in counts:
        most = counts[common]
    results = [
        "Words: " + str(words),
        "Different words: " + str(len(counts)),
        "Times: " + str(times),
        "Most common: " + common,
        "Count: " + str(most),
    ]

    # TODO 3: open REPORT with "w" and write each string of `results` to it,
    # followed by "\n"

    # TODO 4: open SEARCHES with "a" and write one line: `search`, ": ", and
    # `times`, followed by "\n". `times` is a number, so use str(times)

    print()
    print("=" * 50)
    print("BOOK LOG:", name)
    print("=" * 50)
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
