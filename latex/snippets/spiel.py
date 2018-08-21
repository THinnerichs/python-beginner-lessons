

def punkte_zuteilung(ergebnisse, wertfunktion):
    max_wert = -1
    for ergebnis in ergebnisse:
        if wertfunktion(ergebnis) > max_wert:
            max_wert = wertfunktion(ergebnis)
    punkte = []
    for ergebnis in ergebnisse:
        punkte.append(int(wertfunktion(ergebnis) == max_wert))
    return punkte

def punkte_wuerfelmaximum(ergebnisse):
    return punkte_zuteilung(ergebnisse, max)

def punkte_wuerfelsumme(ergebnisse):
    return punkte_zuteilung(ergebnisse, sum)

def anzahl_pasch(liste):
    anzahl = 0
    for elem in liste:
        if liste.count(elem) > anzahl:
            anzahl = liste.count(elem)
    return anzahl

def punkte_paschzahl(ergebnisse):
    return punkte_zuteilung(ergebnisse, anzahl_pasch)

class Wuerfelspiel:
    def __init__(self, runden=10, art="wuerfelsumme"):
        self.runden = runden
        # Punktestand als Liste, Reihenfolge wie in Spielerliste
        self.punktestand = []
        self.spieler = []
        # Art des Spiels als Zeichenkette. Geht eleganter, hier der Einfachkeit halber.
        self.art = art

    def zeige_spielstand(self):
        print ("Es spielen {} Spieler, es verbleiben {} Runden. Aktueller Punktestand:".format(
            len(self.spieler), self.runden))
        for index, spieler in enumerate(self.spieler):
            print ("    {}: {}".format(spieler.name, self.punktestand[index]))

    def add_spieler(self, spieler):
        self.spieler.append(spieler)

    def runde(self):
        ergebnisse = []
        for spieler in self.spieler:
            ergebnisse.append(spieler.wuerfeln())
        self.werten(ergebnisse)
        self.runden -= 1

    def werten(self, ergebnisse):
        punkte = []
        if self.art == "wuerfelsumme":
            punkte = punkte_wuerfelsumme(ergebnisse)
        elif self.art == "wuerfelmaximum":
            punkte = punkte_wuerfelmaximum(ergebnisse)
        elif self.art == "paschzahl":
            punkte = punkte_paschzahl(ergebnisse)
        else:
            print ("Spielart", self.art, "ist nicht definiert! Runde wird nicht gewertet!")
            return
        for index, zahl in enumerate(punkte):
            # punktestand enthält spieler noch nicht
            if len(self.punktestand) == index:
                self.punktestand.append(0)

            self.punktestand[index] += zahl

    def simuliere(self):
        while self.runden > 0:
            self.runde()
            self.zeige_spielstand()
            print ("")

        for index, spieler in enumerate(self.spieler):
            if self.punktestand[index] == max(self.punktestand):
                print ("{} hat gewonnen!".format(spieler.name))
