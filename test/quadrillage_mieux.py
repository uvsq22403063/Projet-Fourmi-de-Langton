import tkinter as tk

color = "#f7f7f7"
taille_carre = 10
larg, haut = 900, 700
k, u = 45, 35
speed = 50
direction = "w"
pauses = True
cases = []
couleur = []

window = tk.Tk()
window.config(bg="lightgrey")
canva = tk.Canvas(window, width=larg, height=haut, bd=0, highlightthickness=0)

vitesse = tk.Label(text=f"Clock Speed: {speed}ms", bg="grey", width=15)

# création du quadrillage avec un répertoire pour les cases. (liste cases)
for i in range(larg // taille_carre):
    colonnes = []
    colonnes_couleur = []
    for j in range(haut // taille_carre):
        x0 = i * 10
        y0 = j * 10
        x1 = (i+1) * 10
        y1 = (j+1) * 10
        carre = canva.create_rectangle(x0, y0, x1, y1, outline="#2ed3cd",
                                       fill=color, width=1)
        colonnes.append(carre)
        colonnes_couleur.append(0)
    cases.append(colonnes)
    couleur.append(colonnes_couleur)


# petit test j'ai ajouté une matrice de 0 de meme
# taille que la matrice de carré pour
# pouvoir reconnaitre les couleur des carrés

couleur[k][u] = 1


def pause():
    """met en pause et restart lorsqu'on appuis une deuxiemme fois"""
    global pauses
    if pauses is False:
        pauses = True
    elif pauses is True:
        pauses = False

    deplacement()


def deplacement():
    """le programme du mouvement est 100% opérationel"""
    global k, u, direction
    if pauses is False:
        if couleur[k][u] == 0:
            canva.itemconfig(cases[k][u], fill="#a8681d")
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
            canva.itemconfig(cases[k][u], fill=color)
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

        canva.after(speed, deplacement)


def skipe():
    """avance le programme d'une itération"""

    global pauses

    for i in range(1):
        pauses = False
        deplacement()
    pauses = True


def undoo():
    """retour à l'itération d'avant"""

    return


def reset():
    """fonction qui reset la grille"""
    global pauses, k, u
    for i in range(len(cases)):
        for j in range(len(cases[0])):
            canva.itemconfig(cases[i][j], fill=color)
            couleur[i][j] = 0
    k, u = 45, 35
    pauses = True

    return


def plus():

    global speed
    if speed >= 2:
        speed -= 1
    else:
        speed == speed
    vitesse.config(text=f"Clock Speed: {speed}ms")


def moins():
    global speed
    speed += 1
    vitesse.config(text=f"Clock Speed: {speed}ms")


# play = tk.Button(window, text="Start", bg="grey", font=("Impact", 14),
#                 bd=0, highlightthickness=0, command=deplacement)

pausse = tk.Button(window, text="Pause/play", bg="grey",
                   fg="#383838", font=("Impact", 14), bd=0,
                   highlightthickness=0, command=pause)
undo = tk.Button(window, text="Undo", bg="grey",
                 fg="#383838", font=("Impact", 14), bd=0,
                 highlightthickness=0, command=undoo)
skip = tk.Button(window, text="Skip", bg="grey",
                 fg="#383838", font=("Impact", 14), bd=0,
                 highlightthickness=0, command=skipe)
resset = tk.Button(window, text="Reset", bg="grey",
                   fg="#383838", font=("Impact", 14), bd=0,
                   highlightthickness=0, command=reset)
vit_plus = tk.Button(window, bg="grey", fg="#383838", text="+",
                     font=("Arial", 14), width=1, height=1, command=plus)
vit_moins = tk.Button(window, bg="grey", fg="#383838", text="-",
                      font=("Arial", 14), width=1, height=1, command=moins)


resset.grid(row=0, column=1)
undo.grid(row=3, column=0)
skip.grid(row=3, column=0, sticky="n")
pausse.grid(row=2, column=0)
vit_moins.grid(row=1, column=0, sticky="sw", padx=30)
vit_plus.grid(row=1, column=0, sticky="s", padx=0)
vitesse.grid(row=1, column=0, sticky="s", pady=50, padx=10)
canva.grid(column=1, row=1, rowspan=4)
window.mainloop()
