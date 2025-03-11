import tkinter as tk
import json

color1 = "black"
color2 = "#ff1b2d"
taille_carre = 10
larg, haut = 900, 700
k, u = 45, 35
speed = 10
itération = 0
direction = "n"
pauses = True
cases = []
couleur = []


window = tk.Tk()
window.title("La Fourmi de Langton")
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
couleur[k][u] = 0


def fleche(dir):
    """Oriente la fourmi selon la direction souhaitée"""
    global k, u
    if dir == "w":
        coor = (k * 10 + 2, u * 10 + 5, k * 10 + 8, u * 10 + 2,
                k * 10 + 6, u * 10 + 5, k * 10 + 8, u * 10 + 8)
    elif dir == "e":
        coor = (k * 10 + 8, u * 10 + 5, k * 10 + 2, u * 10 + 2,
                k * 10 + 4, u * 10 + 5, k * 10 + 2, u * 10 + 8)
    elif dir == "n":
        coor = (k * 10 + 5, u * 10 + 2, k * 10 + 2, u * 10 + 8,
                k * 10 + 5, u * 10 + 6, k * 10 + 8, u * 10 + 8)
    elif dir == "s":
        coor = (k * 10 + 5, u * 10 + 8, k * 10 + 2, u * 10 + 2,
                k * 10 + 5, u * 10 + 4, k * 10 + 8, u * 10 + 2)
    return coor


fourmi = canva.create_polygon(fleche(direction), width=0, fill=color2)


def passage_mural():
    """permet une meilleur lecture du programme
       pour faire passer la bordure à la fourmis"""
    global u, k
    if u > haut // taille_carre - 1:
        u = 0
    elif k > larg // taille_carre - 1:
        k = 0
    elif u < 0:
        u = haut // taille_carre - 1
    elif k < 0:
        k = larg // taille_carre - 1


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
    global k, u, direction, itération, fourmi
    if pauses is False:
        canva.delete(fourmi)
        if couleur[k][u] == 0:
            canva.itemconfig(cases[k][u], fill=color2)
            couleur[k][u] = 1
            if direction == "s":
                direction = "w"
                k -= 1
            elif direction == "w":
                direction = "n"
                u -= 1
            elif direction == "n":
                direction = "e"
                k += 1
            elif direction == "e":
                direction = "s"
                u += 1
        elif couleur[k][u] == 1:
            canva.itemconfig(cases[k][u], fill=color1)
            couleur[k][u] = 0
            if direction == "s":
                direction = "e"
                k += 1
            elif direction == "e":
                direction = "n"
                u -= 1
            elif direction == "n":
                direction = "w"
                k -= 1
            elif direction == "w":
                direction = "s"
                u += 1
        passage_mural()
        fourmi = canva.create_polygon(fleche(direction), width=0, fill=color2)
        canva.after(speed, deplacement)
        itération += 1
        nmb.config(text=f"Itération: {itération}")


def reversse():
    """Retourne aux étapes précédentes"""
    global k, u, direction, itération, fourmi
    if pauses is False and itération >= 1:
        canva.delete(fourmi)
        if direction == "n":
            u += 1
            passage_mural()
            if couleur[k][u] == 0:
                canva.itemconfig(cases[k][u], fill=color2)
                couleur[k][u] = 1
                direction = "e"
            elif couleur[k][u] == 1:
                canva.itemconfig(cases[k][u], fill=color1)
                couleur[k][u] = 0
                direction = "w"
        elif direction == "w":
            k += 1
            passage_mural()
            if couleur[k][u] == 0:
                canva.itemconfig(cases[k][u], fill=color2)
                couleur[k][u] = 1
                direction = "n"
            elif couleur[k][u] == 1:
                canva.itemconfig(cases[k][u], fill=color1)
                couleur[k][u] = 0
                direction = "s"
        elif direction == "e":
            k -= 1
            passage_mural()
            if couleur[k][u] == 0:
                canva.itemconfig(cases[k][u], fill=color2)
                couleur[k][u] = 1
                direction = "s"
            elif couleur[k][u] == 1:
                canva.itemconfig(cases[k][u], fill=color1)
                couleur[k][u] = 0
                direction = "n"
        elif direction == "s":
            u -= 1
            passage_mural()
            if couleur[k][u] == 0:
                canva.itemconfig(cases[k][u], fill=color2)
                couleur[k][u] = 1
                direction = "w"
            elif couleur[k][u] == 1:
                canva.itemconfig(cases[k][u], fill=color1)
                couleur[k][u] = 0
                direction = "e"
        fourmi = canva.create_polygon(fleche(direction), width=0, fill=color2)
        canva.after(speed, reversse)
        itération -= 1
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
    global pauses, k, u, direction, itération, fourmi
    canva.delete(fourmi)
    for i in range(len(cases)):
        for j in range(len(cases[0])):
            canva.itemconfig(cases[i][j], fill=color1)
            couleur[i][j] = 0
    k, u = 45, 35
    pauses = True
    itération = 0
    direction = "n"
    nmb.config(text=f"Itération: {itération}")
    fourmi = canva.create_polygon(fleche(direction), width=0, fill="#ff1b2d")

    return


def moins():
    """Réduit la vitesse de la fourmi"""

    global speed, itération
    if speed >= 2:
        speed -= 1
    else:
        speed == speed
    vitesse.config(text=f"Tps/itération: {speed}ms")
    nmb.config(text=f"Itération: {itération}")


def plus():
    """Augmente la vitesse de la fourmi"""
    global speed, itération
    speed += 1
    vitesse.config(text=f"Tps/itération: {speed}ms")
    nmb.config(text=f"Itération: {itération}")


def save():

    return


def load():

    return

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
vitesse = tk.Label(text=f"Tps/itération: {speed}ms", bg="#251F33", fg=color2, width=15)
nmb = tk.Label(text=f"Itération: {itération}", bg="#251F33", fg=color2, width=15)
vit_plus = tk.Button(window, bg="#251F33", fg=color2, text="+",
                     font=("Arial", 14), activeforeground="#251F33",
                     activebackground=color2, width=1, height=1, command=plus)
vit_moins = tk.Button(window, bg="#251F33", fg=color2, text="-",
                      font=("Arial", 14), width=1, height=1,activeforeground="#251F33",
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

menu_bar.add_command(label="Save", command=save)
menu_bar.add_command(label="Load", command=load)
menu_bar.add_command(label="Quit", command=window.destroy)  # commande

menui.add_cascade(label="File", menu=menu_bar)  # nom du menu

window.config(menu=menui)

canva.grid(column=1, row=1, rowspan=4)
window.mainloop()
