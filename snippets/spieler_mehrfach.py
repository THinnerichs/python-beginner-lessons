from wuerfel import Wuerfel

class Spieler:
    """Repräsentiert einen Spieler.

    Diese Beschreibung ist nützlich für dich und andere Programmierer
    """
    # Konstruktor: Aufgerufen beim "bauen" eines Objekts
    def __init__(self, name):

        # ist der Spielername eine Zeichenkette?
        if not isinstance(name, str):
            print ("Der Spielername war keine Zeichenkette!")

        # erzeugen der Attribute
        self.name = name
        self.wuerfel = []

    def add_wuerfel(self, wuerfel):
        self.wuerfel.append(wuerfel)

    def wuerfeln(self):
        results = []
        for w in self.wuerfel:
            results.append(w.wuerfeln())
        return results

