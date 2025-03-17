import tkinter as tk

larg, haut = 800, 600
x = 0
y = 0
window = tk.Tk()
window.title('Fourmi de Langton')
canva = tk.Canvas(window, bg="white", width=larg, height=haut)
canva_dessus = tk.Canvas(window, bg="red", width=larg, height=haut)


def jouer():
    """ex: while pause = false:
            (programme qui fait avancer fourmis)
            canva.after(500, jouer)"""


def pausse():
    play.grid(row=3, column=4)
    
    pause.grid(row=3, column=2)
    four_plus.grid(row=2, column=1, padx=5, pady=5, sticky='n')
    four_moins.grid(row=2, column=0, padx=5, pady=5, sticky='nw')
    fourmis.grid(row=1, column=0, sticky="s")
    close.grid(row=0, column=0)
    quadrillage()

    canva.grid(row=1, column=2, columnspan=3, rowspan=2)


def nex():
    canva_dessus.destroy()
    pausse()

    return

# Mis cette fonction ici pour voir le rendu


def quadrillage():
    """création d'un quadrillage"""
    global larg, haut
    long_case = 10

    for i in range(0, larg, long_case):
        canva.create_line(i, 0, i, haut, fill="black")

    for j in range(0, larg, long_case):
        canva.create_line(0, j, larg, j, fill="black")


# J'ai créer cette fonction pour voir si la creation de rectangle
# matchais bien avec la cadrillage et ça rend vraiment bien testez et essayez
# de jouer avec les paramettres mais ça va rendre super avec
# cette tecnhique qui est vraiment simple en plus


def ligne_de_rectangle():
    global x, y
    canva.create_rectangle(x, y, x+10, y+10, fill="black")
    x += 10
    canva.after(500, ligne_de_rectangle)


# création des boutons de la fenetre
close = tk.Button(window, bg="red", text="Fermer", fg="black",
                  font=("Arial", 8), command=window.destroy)
play = tk.Button(window, bg="grey", fg="black", text="PLAY",
                 font=("Impact", 14), command=jouer)
pause = tk.Button(window, bg="grey", fg="black", text="PAUSE",
                  font=("Impact", 14), command=pausse)
nexte = tk.Button(canva_dessus, bg="grey", fg="black", text="NEXT",
                  font=("Impact", 14), command=nex)
four_plus = tk.Button(window, bg="grey", fg="black", text="+",
                      font=("Arial", 14), command=nexte)
four_moins = tk.Button(window, bg="grey", fg="black", text="-",
                       font=("Arial", 14), command=nexte)
fourmis = tk.Label(window, text="Fourmis", font=("Arial", 13), bg='grey')


canva_dessus.grid()

nexte.grid(row=3, column=3)

window.mainloop()
