import tkinter as tk

larg, haut = 800, 600


def jouer():

    return


def pausse():

    return


def nex():

    return


window = tk.Tk()
canva = tk.Canvas(window, bg="white", width=larg, height=haut)

# création des boutons de la fenetre
close = tk.Button(window, bg="red", text="Fermer", fg="black",
                  font=("Arial", 8))
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
fourmis = tk.Label(window, text="Fourmis")

play.grid(row=2, column=4)
nexte.grid(row=2, column=3)
pause.grid(row=2, column=2)
four_plus.grid(row=1, column=1, padx=5, pady=5)
four_moins.grid(row=1, column=0, padx=5, pady=5)
fourmis.grid(row=1, column=0)
close.grid(row=0, column=0)

canva.grid(row=1, column=2, columnspan=3)
window.mainloop()
