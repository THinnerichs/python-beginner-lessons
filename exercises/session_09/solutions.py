# -----------
# First Part
# -----------

import random

class Spieler:
    def __init__(self, name):
        self.name = name

    def kniffel_wurf(self):
        seiten = list(range(1, 6))
        return random.choices(seiten, k=5)

EINSER = (lambda wurf: digits(wurf, 1))
ZWEIER = (lambda wurf: digits(wurf, 2))
DREIER = (lambda wurf: digits(wurf, 3))
VIERER = (lambda wurf: digits(wurf, 4))
FUENFER = (lambda wurf: digits(wurf, 5))
SECHSER = (lambda wurf: digits(wurf, 6))

def digits(wurf, zahl):
    return zahl * wurf.count(zahl)

def score(wurf, kategorie):
    return kategorie(wurf)

# -----------
# Second Part
# -----------

DREIERPASCH = (lambda wurf: n_of_a_kind(wurf, 3))
VIERERPASCH = (lambda wurf: n_of_a_kind(wurf, 4))

def n_of_a_kind(wurf, n):
    occ = Counter(wurf).most_common(1)[1]
    if occ == n:
        return sum(wurf)
    return 0

KNIFFEL = (lambda wurf: 50 if Counter(wurf).most_common(1)[1] == 5 else 0)
KLEINE_STRASSE = (lambda wurf: 30 if sorted(wurf) == [1, 2, 3, 4, 5] else 0)
GROSSE_STRASSE = (lambda wurf: 40 if sorted(wurf) == [2, 3, 4, 5, 6] else 0)
CHANCE = sum
