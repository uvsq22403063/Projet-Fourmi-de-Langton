import tkinter as tk

LARGEUR, HAUTEUR = 600, 400
x0, y0 = LARGEUR/2, HAUTEUR/2

root = tk.Tk()
canva = tk.Canvas(root, width=LARGEUR, height=HAUTEUR, bg="red")
canva.grid(rowspan = 50, columnspan = 50)

fourmis = tk.Label(canva, )




#fourmis = canva.create_rectangle(x0 - 5, y0 - 5, x0 + 5, y0 + 5, fill="red")

































root.mainloop()