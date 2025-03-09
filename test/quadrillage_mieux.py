import tkinter as tk

taille_carre = 10
larg, haut = 900, 700
cases = []
couleur = []

window = tk.Tk()
window.config(bg="#102531")
canva = tk.Canvas(window, width=larg, height=haut, bd=0, highlightthickness=0)

test = tk.Label(text="Me voici", bg="#a3491f")

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
                                       fill="#0d5a57", width=1)
        colonnes.append(carre)
        colonnes_couleur.append(0)
    cases.append(colonnes)
    couleur.append(colonnes_couleur)


# petit test j'ai ajouté une matrice de 0 de meme
# taille que la matrice de carré pour
# pouvoir reconnaitre les couleur des carrés
k = 30
u = 30
direction = "e"
pauses = False
couleur[k][u] = 0


def pause():
    """met en pause et restart lorsquon appui une deuxiemme fois"""
    global pauses
    if pauses is False:
        pauses = True
    elif pauses is True:
        pauses = False


def deplacement():
    """le programme du mouvement est 100% opérationel"""
    global k, u, direction
    if pauses is False:
        if k and u >= 0:
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
                canva.itemconfig(cases[k][u], fill="#0d5a57")
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
        else:
            return
    canva.after(2, deplacement)


bouton1 = tk.Button(window, text="Start", bg="#a3491f", font=("Impact", 14),
                    bd=0, highlightthickness=0, command=deplacement)

bouton2 = tk.Button(window, text="Pause/play", bg="#a3491f",
                    font=("Impact", 14), bd=0,
                    highlightthickness=0, command=pause)

bouton2.grid(row=2, column=0)
bouton1.grid(row=1, column=0)


test.grid(row=0, column=0)
canva.grid(column=1, row=0, rowspan=4)
window.mainloop()
