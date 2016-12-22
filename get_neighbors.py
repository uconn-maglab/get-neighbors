#!/usr/bin/env python3


class NeighborHunt:
    def __init__(self, **kwargs):
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

    def find(self):
        for word in self.words:
            wlen = len(word)
            self.neighbors[word] = []
            word = word.split(self.sep)
            for q in self.corpus:
                if len(q) == wlen:
                    self.check_substitution(word, q.split(self.sep))
                elif len(q) == wlen+1:
                    self.check_addition(word, q.split(self.sep))
                elif len(q) == wlen-1:
                    self.check_deletion(word, q.split(self.sep))
                else:
                    continue

    def check_addition(self, base, candidate):
        counter = 0
        # while counter < 2:
            for position in range(len(word)):
                if word[position] == candidate[position+counter]:
                    pass
