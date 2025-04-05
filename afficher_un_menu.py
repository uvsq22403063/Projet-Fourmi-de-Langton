import tkinter as tk
import subprocess

k, u = 45, 35
speed = 10
direction1 = "n"
nbcolor = 4

window = tk.Tk()
window.config(bg="lightgrey")
window.geometry("854x480")

titre = tk.Label(window, text="Choix des variables de bases:",
                 font=("Arial", 18))
titre.grid(row=0, pady=50)


def prout():
    global k, u, speed, direction1, nbcolor
    k, u = int(txt_coordx.get()), int(txt_coordy.get())
    speed = int(txt_speed.get())
    direction1 = str(txt_direc.get())
    nbcolor = int(txt_couleur.get())

    subprocess.run(["python", ".\\test\\couleurs4.py"])
    return


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
label_coordx.pack(side="left", ipadx=20)
txt_coordx = tk.Entry(frame_coord, font=("Arial", 14), width=4)
txt_coordx.pack(side="left", ipadx=20)

label_coordy = tk.Label(frame_coord, text="y(0 à 70):", font=("Arial", 14))
label_coordy.pack(side="left", ipadx=20)
txt_coordy = tk.Entry(frame_coord, font=("Arial", 14), width=4)
txt_coordy.pack(side="left", ipadx=20)

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
label_nb_couleurs = tk.Label(frame_nb_couleur, text="nombre couleurs(2 à 6):",
                             font=("Arial", 14))
label_nb_couleurs.pack(side="left")

txt_couleur = tk.Entry(frame_nb_couleur, font=("Arial", 14))
txt_couleur.pack(side="left")


# bouton jouer
jouer = tk.Button(window, text="launch", command=prout)
jouer.grid(row=4, column=1, padx=100)

# création truc en haut à gauche
menui = tk.Menu(window)
menu_bar = tk.Menu(menui, tearoff=0)

menu_bar.add_command(label="launch", command=prout)
menu_bar.add_command(label="quitter", command=window.destroy)

menui.add_cascade(label="fichier", menu=menu_bar)

window.config(menu=menui)
window.mainloop()
