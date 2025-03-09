import tkinter as tk

taille_carre = 10
larg, haut = 800, 600
colonnes = []
cases = []


window = tk.Tk()
window.config(bg="lightgrey")
canva = tk.Canvas(window, width=larg, height=haut)

test = tk.Label(text="Me voici")

# création du quadrillage avec un répertoire pour les cases. (liste cases)
for i in range(larg // taille_carre):
    colonnes = []
    for j in range(haut // taille_carre):
        x0 = i * 10
        y0 = j * 10
        x1 = (i+1) * 10
        y1 = (j+1) * 10
        carre = canva.create_rectangle(x0, y0, x1, y1, outline="darkgrey",
                                       fill="white", width=1)
        colonnes.append(carre)
    cases.append(colonnes)

canva.itemconfig(cases[1][1], fill="red")

test.grid(row=0, column=0)
canva.grid(column=1)
window.mainloop()
