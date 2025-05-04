import tkinter as tk
import json
import random as rd
import valeurs_variables_menu as vv

vv.charge()

path = ".\\fourmi\\donnee_grille.json"

color1 = "black"
color2 = "#ff1b2d"
taille_carre = 10
larg, haut = 900, 700
nb_fourmis = vv.nbf
nb_finit = 0
x, y = vv.kf, vv.uf
pos_x = []
pos_y = []
posx_init = []
posy_init = []
direction = []
direction_init = []

indice = 0
speed = vv.speedf
itération = 0
direction1 = vv.direction1f
direction2 = "n"
pauses = True
cases = []
couleur = []
fourmis = []
suite = vv.suitef
suite_init = suite
if len(suite) == 2:
    color = ["black", "#ff1b2d"]
elif len(suite) == 3:
    color = ["black", "#ff1b2d", "#25fde9"]
elif len(suite) == 4:
    color = ["black", "yellow", "#ff1b2d", "#25fde9"]
elif len(suite) == 5:
    color = ["black", "yellow", "#ff1b2d", "#8A00C4", "#25fde9"]
elif len(suite) == 6:
    color = ["black", "yellow", "#00ff1a", "#ff1b2d", "#8A00C4", "#25fde9"]

if nb_fourmis == 1:
    k, u = x, y
    pos_x.append(k)
    posx_init.append(k)
    pos_y.append(u)
    posy_init.append(u)
    v = direction1
    direction.append(v)
    direction_init.append(v)
    nb_finit += 1
else:
    for g in range(nb_fourmis):
        k = rd.randint(0, 89)
        u = rd.randint(0, 69)

        pos_x.append(k)
        posx_init.append(k)

        pos_y.append(u)
        posy_init.append(u)
        v = rd.choice(["n", "e", "s", "w"])
        direction.append(v)
        direction_init.append(v)
        nb_finit += 1

color_init = color

window = tk.Tk()
window.title("Fourmi de Langton")
window.config(bg="#0a0a0a")
canva = tk.Canvas(window, width=larg, height=haut, bd=0, highlightthickness=0)


# Création du quadrillage avec un répertoire pour les cases. (liste cases)
for i in range(larg // taille_carre):
    colonnes = []
    colonnes_couleur = []
    for j in range(haut // taille_carre):
        x0 = i * 10
        y0 = j * 10
        x1 = (i+1) * 10
        y1 = (j+1) * 10
        carre = canva.create_rectangle(x0, y0, x1, y1, outline="#251F33",
                                       fill=color1, width=1)
        colonnes.append(carre)
        colonnes_couleur.append(0)
    cases.append(colonnes)
    couleur.append(colonnes_couleur)

# Liste permettant de vérifier la couleur de la case.
couleur[x][y] = 0


def fleche(dir):
    """Oriente la fourmi selon la direction souhaitée"""
    global x, y
    if dir == "w":
        coor = (x * 10 + 2, y * 10 + 5, x * 10 + 8, y * 10 + 2,
                x * 10 + 6, y * 10 + 5, x * 10 + 8, y * 10 + 8)
    elif dir == "e":
        coor = (x * 10 + 8, y * 10 + 5, x * 10 + 2, y * 10 + 2,
                x * 10 + 4, y * 10 + 5, x * 10 + 2, y * 10 + 8)
    elif dir == "n":
        coor = (x * 10 + 5, y * 10 + 2, x * 10 + 2, y * 10 + 8,
                x * 10 + 5, y * 10 + 6, x * 10 + 8, y * 10 + 8)
    elif dir == "s":
        coor = (x * 10 + 5, y * 10 + 8, x * 10 + 2, y * 10 + 2,
                x * 10 + 5, y * 10 + 4, x * 10 + 8, y * 10 + 2)
    return coor


def fleche_init(dir, x, y):
    """Oriente la fourmi selon la direction souhaitée initialement"""
    if dir == "w":
        coor = (x * 10 + 2, y * 10 + 5, x * 10 + 8, y * 10 + 2,
                x * 10 + 6, y * 10 + 5, x * 10 + 8, y * 10 + 8)
    elif dir == "e":
        coor = (x * 10 + 8, y * 10 + 5, x * 10 + 2, y * 10 + 2,
                x * 10 + 4, y * 10 + 5, x * 10 + 2, y * 10 + 8)
    elif dir == "n":
        coor = (x * 10 + 5, y * 10 + 2, x * 10 + 2, y * 10 + 8,
                x * 10 + 5, y * 10 + 6, x * 10 + 8, y * 10 + 8)
    elif dir == "s":
        coor = (x * 10 + 5, y * 10 + 8, x * 10 + 2, y * 10 + 2,
                x * 10 + 5, y * 10 + 4, x * 10 + 8, y * 10 + 2)
    return coor


for i in range(nb_fourmis):
    fleches = canva.create_polygon(fleche_init(direction[i], posx_init[i],
                                   posy_init[i]), width=0,
                                   fill="lightblue")
    fourmis.append(fleches)


def passage_mural(k):
    """permet une meilleur lecture du programme
       pour faire passer la bordure à la fourmis"""
    global pos_x, pos_y, x, y
    if pos_y[k] > haut // taille_carre - 1:
        pos_y[k] = 0
    elif pos_x[k] > larg // taille_carre - 1:
        pos_x[k] = 0
    elif pos_y[k] < 0:
        pos_y[k] = haut // taille_carre - 1
    elif pos_x[k] < 0:
        pos_x[k] = larg // taille_carre - 1


def droite(k):
    """Mouvement couleur blanche"""
    global direction2, pos_x, pos_y, direction
    if direction2 == "s":
        direction[k] = "w"
        pos_x[k] -= 1
    elif direction2 == "w":
        direction[k] = "n"
        pos_y[k] -= 1
    elif direction2 == "n":
        direction[k] = "e"
        pos_x[k] += 1
    elif direction2 == "e":
        direction[k] = "s"
        pos_y[k] += 1


def gauche(k):
    """Mouvement couleur noire"""
    global direction2, pos_x, pos_y, direction
    if direction2 == "s":
        direction[k] = "e"
        pos_x[k] += 1
    elif direction2 == "w":
        direction[k] = "s"
        pos_y[k] += 1
    elif direction2 == "n":
        direction[k] = "w"
        pos_x[k] -= 1
    elif direction2 == "e":
        direction[k] = "n"
        pos_y[k] -= 1


def couleur_suivante(a):
    global suite
    a = a + 1
    if a == len(suite):
        a = 0
    return a


def couleur_precedente(a):
    global suite
    if a == 0:
        a = len(suite)
    a = a - 1
    return a


def pause():
    """Met en pause et restart lorsqu'on appuis une deuxiemme fois"""
    global pauses
    if itération == 0:
        pauses = True
    if pauses is False:
        pauses = True
    elif pauses is True:
        pauses = False

    deplacement()


def pause_reverse():
    """Met en pause et restart la fonction reverse"""
    global pauses
    if pauses is True:
        pauses = False
    elif pauses is False:
        pauses = True

    reversse()


def deplacement():
    """Programme le mouvement de la fourmi"""
    global x, y, direction2, itération, fourmis, indice, suite
    global pos_x, pos_y, direction, nb_fourmis
    if pauses is False:
        for i in range(nb_fourmis):
            indice = i
            x = pos_x[i]
            y = pos_y[i]
            direction2 = direction[i]
            canva.delete(fourmis[i])
            if suite[couleur[x][y]] == "d":
                couleur[x][y] = couleur_suivante(couleur[x][y])
                canva.itemconfig(cases[x][y], fill=color[couleur[x][y]])
                droite(indice)
            elif suite[couleur[x][y]] == "g":
                couleur[x][y] = couleur_suivante(couleur[x][y])
                canva.itemconfig(cases[x][y], fill=color[couleur[x][y]])
                gauche(indice)
            fourmis[i] = canva.create_polygon(fleche(direction[i]), width=0,
                                              fill="lightblue")
            passage_mural(indice)
            itération += 1
        canva.after(speed, deplacement)

        nmb.config(text=f"Itération: {itération}")


def reversse():
    """Retourne aux étapes précédentes"""
    global x, y, direction2, itération, fourmis, pos_x, pos_y, nb_fourmis
    global suite
    if pauses is False and itération >= 1:
        for i in range(nb_fourmis):
            indice = -i-1
            x = pos_x[indice]
            y = pos_y[indice]
            direction2 = direction[indice]
            canva.delete(fourmis[indice])
            if direction2 == "n":
                pos_y[indice] += 1
                passage_mural(indice)
                y = pos_y[indice]
                couleur[x][y] = couleur_precedente(couleur[x][y])
                canva.itemconfig(cases[x][y], fill=color[couleur[x][y]])
                if suite[couleur[x][y]] == "g":
                    direction[indice] = "e"
                elif suite[couleur[x][y]] == "d":
                    direction[indice] = "w"
            elif direction2 == "w":
                pos_x[indice] += 1
                passage_mural(indice)
                x = pos_x[indice]
                couleur[x][y] = couleur_precedente(couleur[x][y])
                canva.itemconfig(cases[x][y], fill=color[couleur[x][y]])
                if suite[couleur[x][y]] == "g":
                    direction[indice] = "n"
                elif suite[couleur[x][y]] == "d":
                    direction[indice] = "s"
            elif direction2 == "e":
                pos_x[indice] -= 1
                passage_mural(indice)
                x = pos_x[indice]
                couleur[x][y] = couleur_precedente(couleur[x][y])
                canva.itemconfig(cases[x][y], fill=color[couleur[x][y]])
                if suite[couleur[x][y]] == "g":
                    direction[indice] = "s"
                elif suite[couleur[x][y]] == "d":
                    direction[indice] = "n"
            elif direction2 == "s":
                pos_y[indice] -= 1
                passage_mural(indice)
                y = pos_y[indice]
                couleur[x][y] = couleur_precedente(couleur[x][y])
                canva.itemconfig(cases[x][y], fill=color[couleur[x][y]])
                if suite[couleur[x][y]] == "g":
                    direction[indice] = "w"
                elif suite[couleur[x][y]] == "d":
                    direction[indice] = "e"
            fourmis[indice] = canva.create_polygon(fleche(direction[indice]),
                                                   width=0, fill="lightblue")
            itération -= 1
        canva.after(speed, reversse)
        nmb.config(text=f"Itération: {itération}")


def skipe():
    """Avance le programme d'une itération"""

    global pauses

    for i in range(1):
        pauses = False
        deplacement()
    pauses = True


def undoo():
    """Retourne à l'itération précédente"""
    global pauses
    for i in range(1):
        pauses = False
        reversse()
    pauses = True


def reset():
    """Fonction qui reconfigure la grille, dans la situation initiale"""
    global pauses, x, y, direction2, itération, speed, pos_y, pos_x
    global direction, fourmis, fleches, nb_fourmis, suite, color
    suite = suite_init
    color = color_init
    for b in range(nb_fourmis):
        canva.delete(fourmis[b])
    nb_fourmis = nb_finit
    fourmis = []
    for m in range(nb_fourmis):
        fleches = canva.create_polygon(fleche_init(direction_init[m],
                                       posx_init[m], posy_init[m]), width=0,
                                       fill="lightblue")
        fourmis.append(fleches)
    pos_x = []
    pos_y = []
    direction = []
    for d in range(nb_fourmis):
        pos_x.append(posx_init[d])
        pos_y.append(posy_init[d])
        direction.append(direction_init[d])
    for i in range(len(cases)):
        for j in range(len(cases[0])):
            canva.itemconfig(cases[i][j], fill=color1)
            couleur[i][j] = 0
    x, y = 33, 33
    pauses = True
    itération = 0
    speed = 10
    direction2 = direction1
    nmb.config(text=f"Itération: {itération}")
    vitesse.config(text=f"Tps/itérations: {speed}ms")


def moins():
    """Réduit la vitesse de la fourmi"""

    global speed, itération
    if speed >= 2:
        speed -= 1
    else:
        speed == speed
    vitesse.config(text=f"Tps/itérations: {speed}ms")
    nmb.config(text=f"Itération: {itération}")


def plus():
    """Augmente la vitesse de la fourmi"""
    global speed, itération
    speed += 1
    vitesse.config(text=f"Tps/itérations: {speed}ms")
    nmb.config(text=f"Itération: {itération}")


def sauvegarde():
    """permet de sauvegarder la grille """
    global pauses, etat_fourmis
    pauses = True
    etat_fourmis = {"couleurs_bg": color1, "couleurs_cases": color2,
                    "coord_x": pos_x, "coord_y": pos_y,
                    "itérations": itération,
                    "direction1": direction1, "direction": direction,
                    "vitesse": speed, "couleur_cases2": couleur,
                    "nb_fourmi": nb_fourmis, "suitesave": suite,
                    "colorsave": color}

    fichier = open(path, 'w')

    json.dump(etat_fourmis, fichier)
    fichier.close()


def charger():
    """permet de recharger la grille """
    global etat_fourmis, color1, color2, x, y, itération, pos_x, pos_y
    global direction1, direction, speed, couleur, cases, suite, color
    global fourmis, pauses, nb_fourmis
    pauses = True
    for k in range(nb_fourmis):
        canva.delete(fourmis[k])
    fichier = open(path, 'r')
    # données = fichier.read()
    etat_fourmis = json.load(fichier)
    fichier.close()

    nb_fourmis = etat_fourmis["nb_fourmi"]
    color1 = etat_fourmis["couleurs_bg"]
    color2 = etat_fourmis["couleurs_cases"]
    color = etat_fourmis["colorsave"]
    suite = etat_fourmis["suitesave"]
    pos_x = etat_fourmis["coord_x"]
    pos_y = etat_fourmis["coord_y"]
    itération = etat_fourmis["itérations"]
    direction1 = etat_fourmis["direction1"]
    direction = etat_fourmis["direction"]
    speed = etat_fourmis["vitesse"]
    couleur = etat_fourmis["couleur_cases2"]

    fourmis = []
    for z in range(nb_fourmis):
        fleches = canva.create_polygon(fleche_init(direction[z],
                                       pos_x[z], pos_y[z]), width=0,
                                       fill="lightblue")
        fourmis.append(fleches)
    vitesse.config(text=f"Tps/itérations: {speed}ms")
    nmb.config(text=f"Itération: {itération}")
    for i in range(len(cases)):

        for m in range(len(cases[i])):
            canva.itemconfig(cases[i][m], fill=color[couleur[i][m]])

# play = tk.Button(window, text="Start", bg="grey", font=("Impact", 14),
#                 bd=0, highlightthickness=0, command=deplacement)


# Reset de la grille
resset = tk.Button(window, text="Reset", bg="#251F33",
                   fg=color2, font=("Impact", 14), bd=1,
                   highlightthickness=0, activeforeground="#251F33",
                   activebackground=color2, command=reset)

# Boutons PLAY/PAUSE et reverse
pausse = tk.Button(window, text="Play/pause", bg="#251F33",
                   fg=color2, font=("Impact", 14), bd=1,
                   highlightthickness=0, activeforeground="#251F33",
                   activebackground=color2, command=pause)
reverse = tk.Button(window, text="Reverse", bg="#251F33",
                    fg=color2, font=("Impact", 14), bd=1,
                    highlightthickness=0, activeforeground="#251F33",
                    activebackground=color2, command=pause_reverse)

# Boutons skip et undo
skip = tk.Button(window, text="Skip", bg="#251F33",
                 fg=color2, font=("Impact", 14), bd=1,
                 highlightthickness=0, activeforeground="#251F33",
                 activebackground=color2, width=7, command=skipe)
undo = tk.Button(window, text="Undo", bg="#251F33",
                 fg=color2, font=("Impact", 14), bd=1,
                 highlightthickness=0, activeforeground="#251F33",
                 activebackground=color2, width=7, command=undoo)

# Vitesse de la clock
vitesse = tk.Label(text=f"Tps/itérations: {speed}ms",
                   bg="#251F33", fg=color2, width=15)
nmb = tk.Label(text=f"Itération: {itération}",
               bg="#251F33", fg=color2, width=15)
vit_plus = tk.Button(window, bg="#251F33", fg=color2, text="+",
                     font=("Arial", 14), activeforeground="#251F33",
                     activebackground=color2,
                     width=1, height=1, command=plus)
vit_moins = tk.Button(window, bg="#251F33", fg=color2, text="-",
                      font=("Arial", 14), width=1, height=1,
                      activeforeground="#251F33",
                      activebackground=color2, command=moins)


# Affichage des labels et boutons ci-dessus

resset.grid(row=0, column=1)

skip.grid(row=3, column=0, sticky="n")
undo.grid(row=3, column=0, sticky="s")

pausse.grid(row=2, column=0)
reverse.grid(row=3, column=0, sticky="s", pady=36)

vitesse.grid(row=1, column=0, sticky="s", pady=50, padx=10)
nmb.grid(row=1, column=0, sticky="s", pady=70, padx=10)
vit_moins.grid(row=1, column=0, sticky="s", padx=10)
vit_plus.grid(row=1, column=0, sticky="sw", padx=30)


# afficher un menu en haut à gauche de l'écran

menui = tk.Menu(window)
menu_bar = tk.Menu(menui, tearoff=0)

menu_bar.add_command(label="Save", command=sauvegarde)
menu_bar.add_command(label="Load", command=charger)
menu_bar.add_command(label="Quit", command=window.destroy)  # commande

menui.add_cascade(label="File", menu=menu_bar)  # nom du menu

window.config(menu=menui)

canva.grid(column=1, row=1, rowspan=4)
window.mainloop()
