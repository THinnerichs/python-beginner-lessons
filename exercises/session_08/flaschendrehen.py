from random import choice, choices, sample

class Flaschendrehen:

    def __init__(self, spieler):
        self.spieler = spieler # liste von spielern

    def zufälliger_spieler(self):
        return choice(self.spieler)

    def simuliere_runden(self, anzahl=5):
        return choices(self.spieler, k=anzahl)

    def simuliere_runden(self, anzahl=5):
        return sample(self.spieler, k=anzahl)
