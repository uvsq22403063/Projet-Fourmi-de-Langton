import tkinter as tk

taille_carre = 10
larg, haut = 800, 600
cases = []
couleur = []

window = tk.Tk()
window.config(bg="lightgrey")
canva = tk.Canvas(window, width=larg, height=haut)

test = tk.Label(text="Me voici")

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

canva.itemconfig(cases[1][1], fill="white")


# petit test j'ai ajouté une matrice de 0 de meme taille que la matrice de carré pour
# pouvoir reconnaitre les couleur des carrés
couleur[1][1] = 0
if couleur[1][1] == 0:
    canva.itemconfig(cases[1][1], fill="black")
    couleur[1][1] = 1
else:
    canva.itemconfig(cases[1][1], fill="white")
    couleur[1][1] = 0









print(couleur)









test.grid(row=0, column=0)
canva.grid(column=1)
window.mainloop()
