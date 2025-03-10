import tkinter as tk

larg, haut = 800, 600

racine = tk.Tk()
racine.config(bg="lightgrey")
racine.title('Test de grille')
canvas = tk.Canvas(racine, bg="white", height=haut, width=larg)

L = 10
couleur = 'white'





haut = (1,0)
bas = (-1,0)
gauche = (10,-10)
droite = (-10,10)
fourmie = (0, 0)
black = ( 0, 0, 0)
withe =(255, 255, 255)
couleur = [ black , withe]  
mon_canvas = tk.canvas(racine ,bg = "black" , width = canvas_width  , height = canvas_height)
mon_canvas.pack()
D = {"haut" : False, "bas" : False, "gauche" : False, "droite" : False }


def deplacement():
    """ permet de deplacer la fourmie """
    global couleur 
    couleur =  couleur [i % len(couleur) ]
    
if couleur == "black":
    D["gauche"] = True
    mon_canvas.move(fourmie,  -10, 10)
else:
    D["droite"] = True
mon_canvas.move(fourmie,  10, -10)




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
