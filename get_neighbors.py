#!/usr/bin/env python3

"""
module: get_neighbor.py
author: R Steiner
license: MIT License, copyright (c) 2016 R Steiner
description: Contains the class NeighborHunt, which finds the
phonological neighbors of a list of words.
"""

import json


class NeighborHunt:
    """
    Finds the phonological neighbors (DAS) of a list of words.

    Methods:
        __init__: Constructor.
        find: Finds the neighbors of the given word list.
    """
    def __init__(self, **kwargs):
        """
        Constructor for class NeighborHunt.

        keyword arguments:
            words -- Path to the file containing the words whose
            neighbors will be found. Should contain phonological forms
            only, one per line.
            corpus -- Path to the file containing the corpus. Phonological
            forms only, one per line.
            sep -- String used to separate phonemes in the phonological forms.
            Can be an empty string (''), which will treat every character as
            an individual phoneme. Defaults to '.'
        """
        words_default = "../databases/iphod/iphod_words_monosyll_phono_only.txt"
        wordfile = kwargs.get("words", words_default)
        corpusfile = kwargs.get("corpus",
                                "../databases/iphod/iphod_words_phono_only.txt")
        self.sep = kwargs.get("sep", ".")
        self.neighbors = {}
        with open(wordfile, "r") as wf:
            self.words = [word[:-1] for word in wf.readlines()]
        with open(corpusfile, "r") as cf:
            self.corpus = [word[:-1] for word in cf.readlines()]

    def find(self, debug=False):
        """
        The main neighbor-finding method.

        Iterates through the word list, comparing each word in the
        corpus to the current word in length, and passing it to the
        appropriate "checker" function, or moving on if its length
        indicates that it is not a neighbor. If the checker returns
        True, then it appends that word to the current word's "neighbor"
        entry.

        keyword arguments:
            debug -- If True, it logs the current word and the words
            being compared to it to the console. Defaults to False.
        """
        for word in self.words:
            print(word) if debug else None
            self.neighbors[word] = []
            wsplit = word.split(self.sep)
            wlen = len(wsplit)
            for q in self.corpus:
                print("\t", q) if debug else None
                qsplit = q.split(self.sep)
                if len(qsplit) == wlen:
                    self.neighbors[word].append(q) if self.check_substitution(wsplit, qsplit) else None
                elif len(qsplit) == wlen+1:
                    self.neighbors[word].append(q) if self.check_addition(wsplit, qsplit) else None
                elif len(qsplit) == wlen-1:
                    self.neighbors[word].append(q) if self.check_deletion(wsplit, qsplit) else None
                else:
                    continue

    def check_addition(self, base, candidate):
        strikes = 0
        for position in range(len(base)):
            while True:
                # If they match, break the while loop and try the next position.
                if base[position] == candidate[position+strikes]:
                    break
                # Otherwise, take a strike and continue on that position,
                # as long as it's the first strike. If it's the second strike,
                # then they are not neighbors, so return False.
                else:
                    strikes += 1
                    if strikes >= 2:
                        return False
        else:
            return True

    def check_deletion(self, base, candidate):
        strikes = 0
        for position in range(len(candidate)):
            while True:
                if base[position+strikes] == candidate[position]:
                    break
                else:
                    strikes += 1
                    if strikes >= 2:
                        return False
        else:
            return True

    def check_substitution(self, base, candidate):
        strikes = 0
        for position in range(len(base)):
            if base[position] == candidate[position]:
                continue
            else:
                strikes += 1
                if strikes >= 2:
                    return False
        else:
            return True

# This is mostly for me. You can use it as an example, but you will likely need
# to tweak it to meet your needs.
# if __name__ == "__main__":
#     mono_neighbors = NeighborHunt()
#     mono_neighbors.find(debug=True)
#     with open("iphod_mono_neighbors.json", "w") as f:
#         json.dump(mono_neighbors.neighbors, f, indent=4)
