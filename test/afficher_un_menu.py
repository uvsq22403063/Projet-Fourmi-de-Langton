import tkinter as tk
import subprocess

kf, uf, speedf, direction1f, nbcolorf = 45, 35, 7, "n", 4


def variables():
    global kf, uf, speedf, direction1f, nbcolorf
    kf, uf = int(txt_coordx.get()), int(txt_coordy.get())
    speedf = int(txt_speed.get())
    direction1f = str(txt_direc.get())
    nbcolorf = int(txt_couleur.get())

    if "n" in direction1f:
        direction1f = "n"
    elif "w" or "o" in direction1f:
        direction1f = "w"
    elif "s" in direction1f:
        direction1f = "s"
    elif "e" in direction1f:
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

    if nbcolorf < 2 or nbcolorf > 6:
        nbcolorf = 2
    elif nbcolorf == 6:
        nbcolorf = (6, 1)

    subprocess.run(["python", ".\\test\\couleurs4.py"])
    return kf, uf, speedf, direction1f, nbcolorf


if __name__ == "__main__":

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
    frame_bg_couleur = tk.Frame(window)
    frame_nb_couleur = tk.Frame(window)

    frame_speed.grid(row=1)
    frame_coord.grid(row=2)
    frame_direc.grid(row=3)
    frame_bg_couleur.grid(row=4)
    frame_nb_couleur.grid(row=5)

    # ajout des labels et champs de texte pour les variables

    # vitesse
    label_speed = tk.Label(frame_speed, text="vitesse (ms):",
                           font=("Arial", 14))
    label_speed.pack(side="left")

    txt_speed = tk.Entry(frame_speed, font=("Arial", 14))
    txt_speed.pack(side="right")

    # coordonées de bases
    label_coordx = tk.Label(frame_coord, text="x(0 à90):", font=("Arial", 14))
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

    # bg couleur
    label_bg_couleurs = tk.Label(frame_bg_couleur, text="couleur de fond:",
                                 font=("Arial", 14))
    label_bg_couleurs.pack(side="left")

    txt_couleur = tk.Entry(frame_bg_couleur, font=("Arial", 14))
    txt_couleur.pack(side="left")

    # nb de couleurs
    label_nb_couleurs = tk.Label(frame_nb_couleur, text="couleurs(2 à 6):",
                                 font=("Arial", 14))
    label_nb_couleurs.pack(side="left")

    txt_couleur = tk.Entry(frame_nb_couleur, font=("Arial", 14))
    txt_couleur.pack(side="left")

    # bouton jouer
    jouer = tk.Button(window, text="launch", command=variables)
    jouer.grid(row=4, column=1, padx=100)

    # création truc en haut à gauche
    menui = tk.Menu(window)
    menu_bar = tk.Menu(menui, tearoff=0)

    menu_bar.add_command(label="launch", command=variables)
    menu_bar.add_command(label="quitter", command=window.destroy)

    menui.add_cascade(label="fichier", menu=menu_bar)

    window.config(menu=menui)
    window.mainloop()
