from matplotlib import pyplot
from spiel_test import erstelle_testspiel
from spieler_mehrfach import Spieler
from wuerfel import Wuerfel

def spielerliste(spiel):
    spielernamen = []
    for spieler in spiel.spieler:
        spielernamen.append(spieler.name)
    return spielernamen

def punktediagramm(spiel):

    spielernamen = spielerliste(spiel)
    print (spielernamen, spiel.punktestand)
    pyplot.plot(spielernamen, spiel.punktestand, "bo")
    pyplot.ylim([0, max(spiel.punktestand) + 2])
    pyplot.xlabel("Spielernummer")
    pyplot.show()

def zeitdiagramm(spiel):

    # enthält eine Liste für jeden Spieler.
    # In jeder solchen  Liste befindet sich für jede Runde (index) der
    # aktuelle Punktestand für diesen Spieler
    punktehistorie = []
    for s in spiel.spieler:
        punktehistorie.append([])

    while spiel.runden > 0:
        spiel.runde()

        for index, punktzahl in enumerate(spiel.punktestand):
            punktehistorie[index].append(punktzahl)

    spiel.zeige_spielstand()
    spielernamen = spielerliste(spiel)

    for index, spielerpunkte in enumerate(punktehistorie):
        pyplot.plot(spielerpunkte, label=spielernamen[index])

    pyplot.legend()
    pyplot.xlabel("Rundenzahl")
    pyplot.ylabel("Punktestand")
    pyplot.show()

spiel = erstelle_testspiel(rundenzahl=100, spielerzahl = 5, spielart = "paschzahl")
#mallory = Spieler("Mallory")
#for i in range(5):
#    mallory.add_wuerfel(Wuerfel(30))
#spiel.add_spieler(mallory)
zeitdiagramm(spiel)
