import tkinter as tk

taille_carre = 10
larg, haut = 900, 700
cases = []
couleur = []

window = tk.Tk()
window.config(bg="#102531")
canva = tk.Canvas(window, width=larg, height=haut)

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
        carre = canva.create_rectangle(x0, y0, x1, y1, outline="darkgrey",
                                       fill="white", width=1)
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

couleur[k][u] = 0


def deplacement():
    """le programme du mouvement est 100% opérationel"""
    global k, u, direction
    if k and u >= 0:
        if couleur[k][u] == 0:
            canva.itemconfig(cases[k][u], fill="black")
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
            canva.itemconfig(cases[k][u], fill="white")
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


deplacement()


test.grid(row=0, column=0)
canva.grid(column=1)
window.mainloop()
