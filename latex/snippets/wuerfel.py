from random import randint

class Wuerfel:
    def __init__(self, seiten):
        self.seiten = seiten

    def wuerfeln(self):
        return randint(1, self.seiten)
