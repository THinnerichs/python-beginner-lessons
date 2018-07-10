from wuerfel import Wuerfel
from spieler_mehrfach import Spieler
from spiel import Wuerfelspiel

def erstelle_testspiel(spielerzahl = 3, rundenzahl = 10, wuerfelzahl = 5, spielart = "wuerfelsumme", wuerfelseiten = 20):

    spiel = Wuerfelspiel(runden=rundenzahl, art=spielart)

    for i in range(spielerzahl):

        spieler = Spieler("Spieler {}".format(i + 1))

        for j in range(wuerfelzahl):
            spieler.add_wuerfel(Wuerfel(wuerfelseiten))

        spiel.add_spieler(spieler)

    return spiel

def main():
    testspiel = erstelle_testspiel()
    testspiel.simuliere()



if __name__ == "__main__":
    main()
