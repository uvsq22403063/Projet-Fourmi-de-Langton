import tkinter as tk

larg, haut = 800, 600

racine = tk.Tk()
racine.config(bg="lightgrey")
racine.title('Test de grille')
canvas = tk.Canvas(racine, bg="white", height=haut, width=larg)

L = 10
couleur = 'white'


D = {"haut" : False, "bas" : False, "gauche" : False, "droite" : False }
if couleur == "black":
    D["gauche"] = True
else:
    D["droite"] = True

L = [ haut , bas , gauche , droite ]
def deplacement():
    """ permet de deplacer la fourmie """
    if  couleur =='white ':

        


def quadrillage():
    """création d'un quadrillage"""
    global larg, haut
    long_case = 25

    for i in range(0, larg, long_case):
        canvas.create_line(i, 0, i, haut, fill="black")

    for j in range(0, larg, long_case):
        canvas.create_line(0, j, larg, j, fill="black")


def ch_couleur():
    """changer la couleur du fond du canva"""
    global couleur
    if couleur == 'white':
        couleur = 'black'
    elif couleur == 'black':
        couleur = 'white'
    canvas.config(bg=couleur)


carre1 = tk.Button(racine, padx=L, pady=L, text="changer couleur",
                   bg="darkgrey", fg='black', command=ch_couleur)

carre1.grid()

canvas.grid(row=0, column=1)
racine.mainloop()
