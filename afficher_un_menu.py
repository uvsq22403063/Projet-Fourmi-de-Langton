import tkinter as tk
import subprocess
from fourmi import valeurs_variables_menu as vv


def variables():
    """récupère les valeurs des variables"""

    kf = int(txt_coordx.get())
    uf = int(txt_coordy.get())
    speedf = int(txt_speed.get())
    direction1f = str(txt_direc.get())
    suitef = str(txt_suite.get())

    if direction1f[0] == "n":
        direction1f = "n"
    elif direction1f[0] == "w" or direction1f[0] == "o":
        direction1f = "w"
    elif direction1f[0] == "s":
        direction1f = "s"
    elif direction1f[0] == "e":
        direction1f = "e"
    else:
        direction1f = "n"

    if speedf < 0:
        speedf = 0

    if kf < 0:
        kf = 0
    elif kf > 90:
        kf = 90

    if uf < 0:
        uf = 0
    elif uf > 70:
        uf = 70

    if len(suitef) > 6:
        suitef = "gd"

    suitef.lower()

    vv.sauvegardes(kf, uf, speedf, direction1f, suitef)

    lancer()


def lancer():
    """lance le programme "couleurs4"""

    subprocess.run(["python", ".\\fourmi\\suite_de_couleurs.py"])


window = tk.Tk()
window.config(bg="lightgrey")
window.geometry("860x480")
titre = tk.Label(window, text="Choix des variables de bases:",
                 font=("Arial", 18))
titre.grid(row=0, pady=50)

# création des frames qui contiennent les ENTRY

frame_speed = tk.Frame(window, height=50, width=20)
frame_coord = tk.Frame(window)
frame_direc = tk.Frame(window)
frame_suite = tk.Frame(window)
frame_nb = tk.Frame(window)

frame_speed.grid(row=1)
frame_coord.grid(row=2)
frame_direc.grid(row=3)
frame_suite.grid(row=4)
frame_nb.grid(row=5)

# ajout des labels et champs de texte pour les variables
# vitesse

label_speed = tk.Label(frame_speed, text="vitesse (ms):",
                       font=("Arial", 14))
label_speed.pack(side="left")
txt_speed = tk.Entry(frame_speed, font=("Arial", 14))
txt_speed.pack(side="right")

# coordonées de bases

label_coordx = tk.Label(frame_coord, text="x(0 à 90):", font=("Arial", 14))
label_coordx.pack(side="left", ipadx=10)
txt_coordx = tk.Entry(frame_coord, font=("Arial", 14), width=4)
txt_coordx.pack(side="left", ipadx=10)

label_coordy = tk.Label(frame_coord, text="y(0 à 70):", font=("Arial", 14))
label_coordy.pack(side="left", ipadx=10)
txt_coordy = tk.Entry(frame_coord, font=("Arial", 14), width=4)
txt_coordy.pack(side="left", ipadx=10)

# direction

label_direc = tk.Label(frame_direc, text="direction au départ:",
                       font=("Arial", 14))
label_direc.pack(side="left")
txt_direc = tk.Entry(frame_direc, font=("Arial", 14))
txt_direc.pack(side="left")

# nb de couleurs

label_suite = tk.Label(frame_suite, text="suite (suite de g et d):",
                       font=("Arial", 14))
label_suite.pack(side="left")
txt_suite = tk.Entry(frame_suite, font=("Arial", 14))
txt_suite.pack(side="left")

# nombre de fourmis

label_nb = tk.Label(frame_nb, text="Nombre de Fourmis:",
                    font=("Arial", 14))
label_nb.pack(side="left")
txt_nb = tk.Entry(frame_nb, font=("Arial", 14))
txt_nb.pack(side="right")

# bouton jouer

jouer = tk.Button(window, text="JOUER", command=variables)
jouer.grid(row=6, column=0, pady=20)

# création truc en haut à gauche

menui = tk.Menu(window)
menu_bar = tk.Menu(menui, tearoff=0)
menu_bar.add_command(label="launch", command=variables)
menu_bar.add_command(label="quitter", command=window.destroy)
menui.add_cascade(label="fichier", menu=menu_bar)
window.config(menu=menui)
window.mainloop()
