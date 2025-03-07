import tkinter as tk
racine = tk.Tk()
racine.title('Test de grille')
Canvas = tk.Canvas(racine, bg = 'white', height = 800, width = 800)
L = 10
couleur = 'white'


def ch_couleur():
    global couleur
    if couleur == 'white':
        couleur = 'black'
    elif couleur == 'black':
        couleur = 'white'
    carre1.config(fg = couleur)


carre1 = tk.Button(Canvas, height=L, width=L, fg='yellow', command=ch_couleur)
Canvas.grid()
carre1.grid(row = 0, column = 0)
racine.mainloop()