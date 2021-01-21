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
