import tkinter as tk
racine = tk.Tk()
racine.title('Test de grille')
Canvas = tk.Canvas(racine, bg = 'white', height = 800, width = 800)
L = 50
couleur = 'white'


def ch_couleur():
    global couleur
    if couleur == 'white':
        couleur = 'black'
    elif couleur == 'black':
        couleur = 'white'
    carre.config(bg = couleur)


carre = tk.Button(Canvas, height=L, width=L, bg=couleur, command=ch_couleur)
Canvas.grid()
carre.grid(row=0, column=0)
racine.mainloop()