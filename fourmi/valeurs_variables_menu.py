import json

path = ".\\fourmi\\valeurs.json"

kf, uf, speedf, direction1f, suitef, nbf = 0, 0, 0, 0, 0, 0


def sauvegardes(k, u, speed, direction1, suite, nb):
    """permet de sauvegarder les variables """

    variables = {"kf": k, "uf": u, "speedf": speed,
                 "direction1f": direction1, "suitef": suite, "nbf": nb}

    fichier = open(path, 'w')

    json.dump(variables, fichier)
    print("sauvegarde des variables")
    fichier.close()


def charge():
    """permet de charger les variables """
    global kf, uf, speedf, direction1f, suitef, nbf

    fichier = open(path, 'r')

    variables = json.load(fichier)

    kf = variables["kf"]
    uf = variables["uf"]
    speedf = variables["speedf"]
    direction1f = variables["direction1f"]
    suitef = variables["suitef"]
    nbf = variables["nbf"]

    if kf is None:
        kf = 45
    if uf is None:
        uf = 35
    if speedf is None:
        speedf = 10
    if direction1f is None:
        direction1f = "n"
    if suitef is None:
        suitef = "gd"
    if nbf is None:
        nbf = 1

    fichier.close()
