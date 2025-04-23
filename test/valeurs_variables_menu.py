import json

kf, uf, speedf, direction1f, suitef = 0, 0, 0, 0, 0


def sauvegardes(k, u, speed, direction1, suite):
    """permet de sauvegarder les variables """

    variables = {"kf": k, "uf": u, "speedf": speed,
                 "direction1f": direction1, "suitef": suite}

    fichier = open('valeurs.json', 'w')

    json.dump(variables, fichier)
    print("sauvegarde des variables")
    fichier.close()


def charge():
    """permet de charger les variables """
    global kf, uf, speedf, direction1f, suitef

    fichier = open('valeurs.json', 'r')

    variables = json.load(fichier)

    kf = variables["kf"]
    uf = variables["uf"]
    speedf = variables["speedf"]
    direction1f = variables["direction1f"]
    suitef = variables["suitef"]

    fichier.close()
