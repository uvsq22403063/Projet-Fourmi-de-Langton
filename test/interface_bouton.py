import tkinter as tk

larg, haut = 800, 600
x = 0
y = 0
window = tk.Tk()
window.title('Fourmi de Langton')
canva = tk.Canvas(window, bg="white", width=larg, height=haut)
canva_dessus = tk.Canvas(window, bg="red", width=larg, height=haut)


def jouer():

    return


def pausse():

    global tt_boutons
    canva = tk.Canvas(window, bg="white", width=larg, height=haut)

    color2 = "#ff1b2d"
    speed = 10
    itération = 0

    # play = tk.Button(window, text="Start", bg="grey", font=("Impact", 14),
    #                 bd=0, highlightthickness=0, command=deplacement)

    # Reset de la grille
    resset = tk.Button(window, text="Reset", bg="#251F33",
                       fg=color2, font=("Impact", 14), bd=1,
                       highlightthickness=0, activeforeground="#251F33",
                       activebackground=color2, command=jouer)

    # Boutons PLAY/PAUSE et reverse
    pause = tk.Button(window, text="Play/pause", bg="#251F33",
                      fg=color2, font=("Impact", 14), bd=1,
                      highlightthickness=0, activeforeground="#251F33",
                      activebackground=color2, command=jouer)
    reverse = tk.Button(window, text="Reverse", bg="#251F33",
                        fg=color2, font=("Impact", 14), bd=1,
                        highlightthickness=0, activeforeground="#251F33",
                        activebackground=color2, command=jouer)

    # Boutons skip et undo
    skip = tk.Button(window, text="Skip", bg="#251F33",
                     fg=color2, font=("Impact", 14), bd=1,
                     highlightthickness=0, activeforeground="#251F33",
                     activebackground=color2, width=7, command=jouer)
    undo = tk.Button(window, text="Undo", bg="#251F33",
                     fg=color2, font=("Impact", 14), bd=1,
                     highlightthickness=0, activeforeground="#251F33",
                     activebackground=color2, width=7, command=jouer)

    # Vitesse de la clock
    vitesse = tk.Label(text=f"Tps/itération: {speed}ms",
                       bg="#251F33", fg=color2, width=15)
    nmb = tk.Label(text=f"Itération: {itération}",
                   bg="#251F33", fg=color2, width=15)
    vit_plus = tk.Button(window, bg="#251F33", fg=color2, text="+",
                         font=("Arial", 14), activeforeground="#251F33",
                         activebackground=color2,
                         width=1, height=1, command=jouer)
    vit_moins = tk.Button(window, bg="#251F33", fg=color2, text="-",
                          font=("Arial", 14), width=1, height=1,
                          activeforeground="#251F33",
                          activebackground=color2, command=jouer)
    delte = tk.Button(window, bg="#251F33", fg=color2, text="delete",
                      font=("Arial", 14), activeforeground="#251F33",
                      activebackground=color2, command=destroi)

    # Affichage des labels et boutons ci-dessus

    resset.grid(row=0, column=1)

    skip.grid(row=3, column=0, sticky="n")
    undo.grid(row=3, column=0, sticky="s")

    pause.grid(row=2, column=0)
    reverse.grid(row=3, column=0, sticky="s", pady=36)

    vitesse.grid(row=1, column=0, sticky="s", pady=50, padx=10)
    nmb.grid(row=1, column=0, sticky="s", pady=70, padx=10)
    vit_moins.grid(row=1, column=0, sticky="s", padx=10)
    vit_plus.grid(row=1, column=0, sticky="sw", padx=30)
    delte.grid(row=0, column=0)

    window.config(menu=menui)

    canva.grid(column=1, row=1, rowspan=4)
    tt_boutons = [resset, pause, reverse, skip, undo, vit_moins, vit_plus,
                  vitesse, nmb, canva, delte]


def destroi():
    global tt_boutons, canva_dessus

    for i in range(len(tt_boutons)):
        tt_boutons[i].destroy()

    canva_dessus = tk.Canvas(window, bg="red", width=larg, height=haut)
    canva_dessus.grid(row=0, column=0)

    return


def nex():
    canva_dessus.destroy()
    pausse()

    return


# création des boutons de la fenetre
close = tk.Button(window, bg="red", text="Fermer", fg="black",
                  font=("Arial", 8), command=window.destroy)

nexte = tk.Button(window, bg="grey", fg="black", text="NEXT",
                  font=("Impact", 14), command=nex)

# afficher un menu en haut à gauche de l'écran

menui = tk.Menu(window)
menu_bar = tk.Menu(menui, tearoff=0)

menu_bar.add_command(label="New", command=destroi)
menu_bar.add_command(label="Save", command=jouer)
menu_bar.add_command(label="Load", command=jouer)
menu_bar.add_command(label="Quit", command=window.destroy)  # Commandes

menui.add_cascade(label="File", menu=menu_bar)  # nom du menu

window.config(menu=menui)

canva_dessus.grid(row=0, column=0)

nexte.grid(row=3, column=3)

window.mainloop()
