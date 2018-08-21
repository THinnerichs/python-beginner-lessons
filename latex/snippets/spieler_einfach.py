from wuerfel import Wuerfel

class Spieler:
    """Repräsentiert einen Spieler.

    Diese Beschreibung ist nützlich für dich und andere Programmierer
    """
    # Konstruktor: Aufgerufen beim "bauen" eines Objekts
    def __init__(self, name, wuerfel):

        # ist der Spielername eine Zeichenkette?
        if not isinstance(name, str):
            print ("Der Spielername war keine Zeichenkette!")

        # ist der würfel wirklich ein würfel?
        if not isinstance(wuerfel, Wuerfel):
            print ("Das war kein wuerfel!")
            # in richtigem Programm: Fehlerbehandlung / Exceptions

        # erzeugen der Attribute
        self.name = name
        self.wuerfel = wuerfel

    def wuerfel_wecheln(self, wuerfel):
        self.wuerfel = wuerfel

    def wuerfeln(self):
        return self.wuerfel.wuerfeln()

