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

    def find(self, debug=False):
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
        # position = 0
        # while strikes < 2 and position < len(base):
        for position in range(len(base)):
            # for position in range(len(word)):
            if base[position] == candidate[position+strikes]:
                # position += 1
                continue
            else:
                strikes += 1
                # position += 1
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
                    # continue
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

if __name__ == "__main__":
    neighbor_test = NeighborHunt(words="tests/test_monos.txt",
                                 corpus="tests/iphod_subset.txt")
    neighbor_test.find(debug=True)
