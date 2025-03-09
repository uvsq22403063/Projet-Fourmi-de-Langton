import tkinter as tk

larg, haut = 800, 600


def jouer():
    """ex: while pause = false:
            (programme qui fait avancer fourmis)
            canva.after(500, jouer)"""

    return


def pausse():
    """On fait un truc du genre avec un booléen et on met un while dans jouer
       ex : pause = true"""

    return


def nex():
    """on dit que se bouton est activable que si jouer est en pause
       et genre ici on met un if pour check si c'est en pause et si oui alors on fait avancer la fourmis
       sinon il se passe rien
       ex: if pause == true:
            programme qui fait avancer fourmis d'un mouvement
           else:
            il se passe rien(peut être même pas besoin de mettre else)"""

    return


window = tk.Tk()
window.title('Fourmi de Langton')
canva = tk.Canvas(window, bg="white", width=larg, height=haut)

# Mis cette fonction ici pour voir le rendu


def quadrillage():
    """création d'un quadrillage"""
    global larg, haut
    long_case = 20

    for i in range(0, larg, long_case):
        canva.create_line(i, 0, i, haut, fill="black")

    for j in range(0, larg, long_case):
        canva.create_line(0, j, larg, j, fill="black")


# création des boutons de la fenetre
close = tk.Button(window, bg="red", text="Fermer", fg="black",
                  font=("Arial", 8), command=window.destroy)
play = tk.Button(window, bg="grey", fg="black", text="PLAY",
                 font=("Impact", 14), command=jouer)
pause = tk.Button(window, bg="grey", fg="black", text="PAUSE",
                  font=("Impact", 14), command=pausse)
nexte = tk.Button(window, bg="grey", fg="black", text="NEXT",
                  font=("Impact", 14), command=nex)
four_plus = tk.Button(window, bg="grey", fg="black", text="+",
                      font=("Impact", 14), command=nexte)
four_moins = tk.Button(window, bg="grey", fg="black", text="-",
                       font=("Impact", 14), command=nexte)
fourmis = tk.Label(window, text="Fourmis", font=("Arial", 13), bg='grey')

play.grid(row=3, column=4)
nexte.grid(row=3, column=3)
pause.grid(row=3, column=2)
four_plus.grid(row=2, column=1, padx=5, pady=5, sticky='n')
four_moins.grid(row=2, column=0, padx=5, pady=5, sticky='nw')
fourmis.grid(row=1, column=0, sticky="s")
close.grid(row=0, column=0)
quadrillage()
canva.grid(row=1, column=2, columnspan=3, rowspan=2)
window.mainloop()
