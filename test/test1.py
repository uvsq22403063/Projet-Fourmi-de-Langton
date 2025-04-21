import tkinter as tk
import random
import json


color1 = "black"
color2 = "#ff1b2d"
taille_carre = 10
larg, haut = 900, 700
k, u = 45, 35
speed = 10
nombre_four = 0
itération = 0
direction1 = "n"
direction2 = "n"
pauses = True
cases = []
couleur = []
nb_fourmies = []


window = tk.Tk()
window.title("Fourmi de Langton")
window.config(bg="#0a0a0a")
canva = tk.Canvas(window, width=larg, height=haut, bd=0, highlightthickness=0)


# Création du quadrillage avec un répertoire pour les cases. (liste cases)
for i in range(larg // taille_carre):
    colonnes = []
    colonnes_couleur = []
    for j in range(haut // taille_carre):
        x0 = i * 10
        y0 = j * 10
        x1 = (i+1) * 10
        y1 = (j+1) * 10
        carre = canva.create_rectangle(x0, y0, x1, y1, outline="#251F33",
                                       fill=color1, width=1)
        colonnes.append(carre)
        colonnes_couleur.append(0)
    cases.append(colonnes)
    couleur.append(colonnes_couleur)

# Liste permettant de vérifier la couleur de la case.
couleur[k][u] = 0

etat_fourmis = {"couleurs_bg": color1, "couleurs_cases": color2,
                "couleur_cases2": couleur, "coord_x": k, "coord_y": u,
                "itérations": itération, "direction1": direction1,
                "direction2": direction2, "vitesse": speed}


def fleche(dir):
    """Oriente la fourmi selon la direction souhaitée"""
    global k, u
    if dir == "w":
        coor = (k * 10 + 2, u * 10 + 5, k * 10 + 8, u * 10 + 2,
                k * 10 + 6, u * 10 + 5, k * 10 + 8, u * 10 + 8)
    elif dir == "e":
        coor = (k * 10 + 8, u * 10 + 5, k * 10 + 2, u * 10 + 2,
                k * 10 + 4, u * 10 + 5, k * 10 + 2, u * 10 + 8)
    elif dir == "n":
        coor = (k * 10 + 5, u * 10 + 2, k * 10 + 2, u * 10 + 8,
                k * 10 + 5, u * 10 + 6, k * 10 + 8, u * 10 + 8)
    elif dir == "s":
        coor = (k * 10 + 5, u * 10 + 8, k * 10 + 2, u * 10 + 2,
                k * 10 + 5, u * 10 + 4, k * 10 + 8, u * 10 + 2)
    return coor


fourmi = canva.create_polygon(fleche(direction2), width=0, fill="lightblue")

def fleche_dir(k, u, dir):
    if dir == "w":
        return (k * 10 + 2, u * 10 + 5, k * 10 + 8, u * 10 + 2,
                k * 10 + 6, u * 10 + 5, k * 10 + 8, u * 10 + 8)
    elif dir == "e":
        return (k * 10 + 8, u * 10 + 5, k * 10 + 2, u * 10 + 2,
                k * 10 + 4, u * 10 + 5, k * 10 + 2, u * 10 + 8)
    elif dir == "n":
        return (k * 10 + 5, u * 10 + 2, k * 10 + 2, u * 10 + 8,
                k * 10 + 5, u * 10 + 6, k * 10 + 8, u * 10 + 8)
    elif dir == "s":
        return (k * 10 + 5, u * 10 + 8, k * 10 + 2, u * 10 + 2,
                k * 10 + 5, u * 10 + 4, k * 10 + 8, u * 10 + 2)



def passage_mural():
    """permet une meilleur lecture du programme
       pour faire passer la bordure à la fourmis"""
    global u, k
    if u > haut // taille_carre - 1:
        u = 0
    elif k > larg // taille_carre - 1:
        k = 0
    elif u < 0:
        u = haut // taille_carre - 1
    elif k < 0:
        k = larg // taille_carre - 1


def pause():
    """met en pause ou démarre, et si y'a plus d'une fourmie, elle pop"""
    global pauses
    if pauses == True:
        pauses = False
    else:
        pauses = True

    if nombre_four > 1:
        generer_fourmis()
        deplacement_multi()
    else:
        deplacement()


def pause_reverse():
    """Met en pause et restart la fonction reverse"""
    global pauses
    if pauses is True:
        pauses = False
    elif pauses is False:
        pauses = True

    reversse()


def deplacement():
    """Programme le mouvement de la fourmi"""
    global k, u, direction2, itération, fourmi
    if pauses is False:
        canva.delete(fourmi)
        if couleur[k][u] == 0:
            canva.itemconfig(cases[k][u], fill=color2)
            couleur[k][u] = 1
            if direction2 == "s":
                direction2 = "w"
                k -= 1
            elif direction2 == "w":
                direction2 = "n"
                u -= 1
            elif direction2 == "n":
                direction2 = "e"
                k += 1
            elif direction2 == "e":
                direction2 = "s"
                u += 1
        elif couleur[k][u] == 1:
            canva.itemconfig(cases[k][u], fill=color1)
            couleur[k][u] = 0
            if direction2 == "s":
                direction2 = "e"
                k += 1
            elif direction2 == "e":
                direction2 = "n"
                u -= 1
            elif direction2 == "n":
                direction2 = "w"
                k -= 1
            elif direction2 == "w":
                direction2 = "s"
                u += 1
        passage_mural()
        fourmi = canva.create_polygon(fleche(direction2), width=0,
                                      fill="lightblue")
        canva.after(speed, deplacement)
        itération += 1
        nmb.config(text=f"Itération: {itération}")


def deplacement_multi():
    """focntion qui permet de deplacer plusieur fourmies en meme temps """
    global fourmis, couleur, cases, itération
    if pauses == False:
        for f in fourmis:
            canva.delete(f["poly"])
            k = f["x"]
            u = f["y"]
            direction2 = f["dir"]

            if couleur[k][u] == 0:
                canva.itemconfig(cases[k][u], fill=color2)
                couleur[k][u] = 1
                if direction2 == "s":
                    direction2 = "w"
                    k -=  1
                elif direction2 == "w":
                    direction2 = "n"
                    u -=  1
                elif direction2 == "n":
                    direction2 = "e"
                    k +=  1
                elif direction2 == "e":
                    direction2 = "s"
                    u +=  1
            elif couleur[k][u] == 1:
                canva.itemconfig(cases[k][u], fill=color1)
                couleur[k][u] = 0
                if direction2 == "s":
                    direction2 = "e"
                    k +=  1
                elif direction2 == "e":
                    direction2 = "n"
                    u -=  1
                elif direction2 == "n":
                    direction2 = "w"
                    k -=  1
                elif direction2 == "w":
                    direction2 = "s"
                    u +=  1

            if k > larg // taille_carre - 1:
                k = 0
            elif k < 0:
                k = larg // taille_carre - 1
            if u > haut // taille_carre - 1:
                u = 0
            elif u < 0:
                u = haut // taille_carre - 1

            f["x"] = k
            f["y"] = u
            f["dir"] = direction2
            f["poly"] = canva.create_polygon(fleche_dir(k, u, direction2), width=0, fill="lightblue")

        itération = itération + 1
        nmb.config(text=f"Itération: {itération}")
        canva.after(speed, deplacement_multi)
    
   



def reversse():
    """Retourne aux étapes précédentes"""
    global k, u, direction2, itération, fourmi
    if pauses is False and itération >= 1:
        canva.delete(fourmi)
        if direction2 == "n":
            u += 1
            passage_mural()
            if couleur[k][u] == 0:
                canva.itemconfig(cases[k][u], fill=color2)
                couleur[k][u] = 1
                direction2 = "e"
            elif couleur[k][u] == 1:
                canva.itemconfig(cases[k][u], fill=color1)
                couleur[k][u] = 0
                direction2 = "w"
        elif direction2 == "w":
            k += 1
            passage_mural()
            if couleur[k][u] == 0:
                canva.itemconfig(cases[k][u], fill=color2)
                couleur[k][u] = 1
                direction2 = "n"
            elif couleur[k][u] == 1:
                canva.itemconfig(cases[k][u], fill=color1)
                couleur[k][u] = 0
                direction2 = "s"
        elif direction2 == "e":
            k -= 1
            passage_mural()
            if couleur[k][u] == 0:
                canva.itemconfig(cases[k][u], fill=color2)
                couleur[k][u] = 1
                direction2 = "s"
            elif couleur[k][u] == 1:
                canva.itemconfig(cases[k][u], fill=color1)
                couleur[k][u] = 0
                direction2 = "n"
        elif direction2 == "s":
            u -= 1
            passage_mural()
            if couleur[k][u] == 0:
                canva.itemconfig(cases[k][u], fill=color2)
                couleur[k][u] = 1
                direction2 = "w"
            elif couleur[k][u] == 1:
                canva.itemconfig(cases[k][u], fill=color1)
                couleur[k][u] = 0
                direction2 = "e"
        fourmi = canva.create_polygon(fleche(direction2), width=0,
                                      fill="lightblue")
        canva.after(speed, reversse)
        itération -= 1
        nmb.config(text=f"Itération: {itération}")


def skipe():
    """Avance le programme d'une itération"""

    global pauses

    for i in range(1):
        pauses = False
        deplacement()
    pauses = True


def undoo():
    """Retourne à l'itération précédente"""
    global pauses
    for i in range(1):
        pauses = False
        reversse()
    pauses = True


def reset():
    """Fonction qui reconfigure la grille, dans la situation initiale"""
    global pauses, k, u, direction2, itération, fourmi, speed,canvas , nb_fourmie
    canva.delete(fourmi)
    for i in range(len(cases)):
        for j in range(len(cases[0])):
            canva.itemconfig(cases[i][j], fill=color1)
            couleur[i][j] = 0
    k, u = 45, 35
    pauses = True
    itération = 0
    speed = 10
    direction2 = direction1
    nmb.config(text=f"Itération: {itération}")
    vitesse.config(text=f"Tps/Itérations: {speed}")

    fourmi = canva.create_polygon(fleche(direction2), width=0,
                                  fill="lightblue")
    nb_fourmies.append(fourmi)
    for i in nb_fourmie:
        canvas.delete(i)
    nb_fourmie.clear()


def moins():
    """Réduit la vitesse de la fourmi"""

    global speed, itération
    if speed >= 2:
        speed -= 1
    else:
        speed == speed
    vitesse.config(text=f"Tps/itération: {speed}ms")
    nmb.config(text=f"Itération: {itération}")


def plus():
    """Augmente la vitesse de la fourmi"""
    global speed, itération
    speed += 1
    vitesse.config(text=f"Tps/itération: {speed}ms")
    nmb.config(text=f"Itération: {itération}")


def sauvegarde():
    """permet de sauvegarder la grille """
    global pauses, etat_fourmis
    pauses = True
    etat_fourmis = {"couleurs_bg": color1, "couleurs_cases": color2,
                    "coord_x": k, "coord_y": u, "itérations": itération,
                    "direction1": direction1, "direction2": direction2,
                    "vitesse": speed, "couleur_cases2": couleur}

    fichier = open('donnee_grille.json', 'w')

    json.dump(etat_fourmis, fichier)
    print("sauvegarde de la grille ")
    fichier.close()


def charger():
    """permet de recharger la grille """
    global etat_fourmis, color1, color2, k, u, itération
    global direction1, direction2, speed, couleur, cases
    global fourmi, pauses
    pauses = True
    canva.delete(fourmi) 

    fichier = open('donnee_grille.json', 'r')
    # données = fichier.read()
    etat_fourmis = json.load(fichier)
    fichier.close()

    color1 = etat_fourmis["couleurs_bg"]
    color2 = etat_fourmis["couleurs_cases"]
    k = etat_fourmis["coord_x"]
    u = etat_fourmis["coord_y"]
    itération = etat_fourmis["itérations"]
    direction1 = etat_fourmis["direction1"]
    direction2 = etat_fourmis["direction2"]
    speed = etat_fourmis["vitesse"]
    couleur = etat_fourmis["couleur_cases2"]

    vitesse.config(text=f"Tps/itération: {speed}ms")
    nmb.config(text=f"Itération: {itération}")
    fourmi = canva.create_polygon(fleche(direction2), width=0,
                                  fill="lightblue")
    for i in range(len(cases)):

        for v in range(len(cases[i])):
            if couleur[i][v] == 0:
                canva.itemconfig(cases[i][v], fill=color1)
            else:
                canva.itemconfig(cases[i][v], fill=color2)

    print("chargement de la grille")



#""" cree d'autre fourmie 
def nombre_fourmie():
    """ permet de  demander a l'utilisateur a nombre de fourmie """
    nombre_fourmie= int(input("nombre de fourmie"))
    return nombre_fourmie

def moins_f():
    """Réduit la vitesse de la fourmi"""

    global nombre_four
    if nombre_four >= 2:
        nombre_four -= 1
    else:
        nombre_four == nombre_four
    nb_fourmie.config(text=f"Nombre de fourmie : {nombre_four}")


def plus_f():
    """Augmente la vitesse de la fourmi"""
    global nombre_four
    nombre_four += 1
    nb_fourmie.config(text=f"Nombre de fourmie : {nombre_four}")


fourmis = []
def generer_fourmis():
    global fourmis, nombre_four
    fourmis.clear()
    for _ in range(nombre_four):
        x = random.randint(0, larg // taille_carre - 1)
        y = random.randint(0, haut // taille_carre - 1)
        direction = random.choice(["n", "s", "e", "w"])
        poly = canva.create_polygon(fleche_dir(x, y, direction), width=0, fill="lightblue")
        fourmis.append({"x": x, "y": y, "dir": direction, "poly": poly})

# nb_fourmie = tk.Button(window, text="nombre de fourmie", bg="#251F33",
#                    fg=color2, font=("Impact", 14), bd=1,
#                    highlightthickness=0, activeforeground="#251F33",
#                    activebackground=color2, command=nombre_fourmie)
# nb fourmie
nb_fourmie = tk.Label(text=f"Nombre de fourmie : {nombre_four}",
               bg="#251F33", fg=color2, width=15)
nb_fourmie_plus = tk.Button(window, bg="#251F33", fg=color2, text="+",
                     font=("Arial", 14), activeforeground="#251F33",
                     activebackground=color2,
                     width=1, height=1, command=plus_f)
nb_fourmie_moins = tk.Button(window, bg="#251F33", fg=color2, text="-",
                      font=("Arial", 14), width=1, height=1,
                      activeforeground="#251F33",
                      activebackground=color2, command=moins_f)

# play = tk.Button(window, text="Start", bg="grey", font=("Impact", 14),
#                 bd=0, highlightthickness=0, command=deplacement)


# Reset de la grille
resset = tk.Button(window, text="Reset", bg="#251F33",
                   fg=color2, font=("Impact", 14), bd=1,
                   highlightthickness=0, activeforeground="#251F33",
                   activebackground=color2, command=reset)

# Boutons PLAY/PAUSE et reverse
pausse = tk.Button(window, text="Play/pause", bg="#251F33",
                   fg=color2, font=("Impact", 14), bd=1,
                   highlightthickness=0, activeforeground="#251F33",
                   activebackground=color2, command=pause)
reverse = tk.Button(window, text="Reverse", bg="#251F33",
                    fg=color2, font=("Impact", 14), bd=1,
                    highlightthickness=0, activeforeground="#251F33",
                    activebackground=color2, command=pause_reverse)

# Boutons skip et undo
skip = tk.Button(window, text="Skip", bg="#251F33",
                 fg=color2, font=("Impact", 14), bd=1,
                 highlightthickness=0, activeforeground="#251F33",
                 activebackground=color2, width=7, command=skipe)
undo = tk.Button(window, text="Undo", bg="#251F33",
                 fg=color2, font=("Impact", 14), bd=1,
                 highlightthickness=0, activeforeground="#251F33",
                 activebackground=color2, width=7, command=undoo)

# Vitesse de la clock
vitesse = tk.Label(text=f"Tps/itération: {speed}ms",
                   bg="#251F33", fg=color2, width=15)
nmb = tk.Label(text=f"Itération: {itération}",
               bg="#251F33", fg=color2, width=15)
vit_plus = tk.Button(window, bg="#251F33", fg=color2, text="+",
                     font=("Arial", 14), activeforeground="#251F33",
                     activebackground=color2,
                     width=1, height=1, command=plus)
vit_moins = tk.Button(window, bg="#251F33", fg=color2, text="-",
                      font=("Arial", 14), width=1, height=1,
                      activeforeground="#251F33",
                      activebackground=color2, command=moins)


# Affichage des labels et boutons ci-dessus

nb_fourmie.grid(row=3, column=0, sticky="s", pady=150, padx=10)
nb_fourmie_plus.grid(row=3, column=0, sticky="s",pady=110, padx=10)
nb_fourmie_moins.grid(row=3, column=0, sticky="sw",pady=110, padx=30)

resset.grid(row=0, column=1)

skip.grid(row=3, column=0, sticky="n")
undo.grid(row=3, column=0, sticky="s")

pausse.grid(row=2, column=0)
reverse.grid(row=3, column=0, sticky="s", pady=36)

vitesse.grid(row=1, column=0, sticky="s", pady=50, padx=10)
nmb.grid(row=1, column=0, sticky="s", pady=70, padx=10)
vit_moins.grid(row=1, column=0, sticky="s", padx=10)
vit_plus.grid(row=1, column=0, sticky="sw", padx=30)


# afficher un menu en haut à gauche de l'écran

menui = tk.Menu(window)
menu_bar = tk.Menu(menui, tearoff=0)

menu_bar.add_command(label="Save", command=sauvegarde)
menu_bar.add_command(label="Load", command=charger)
menu_bar.add_command(label="Quit", command=window.destroy)  # commande

menui.add_cascade(label="File", menu=menu_bar)  # nom du menu

window.config(menu=menui)

canva.grid(column=1, row=1, rowspan=4)
window.mainloop()
