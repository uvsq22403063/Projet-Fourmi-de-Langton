import tkinter as tk

window = tk.Tk()
canva = tk.Canvas(window, width=720, height=480, bg="lightblue")


def prout():

    return


menui = tk.Menu(window)
menu_bar = tk.Menu(menui, tearoff=0)

menu_bar.add_command(label="test", command=prout)
menu_bar.add_command(label="quitter", command=window.destroy)

menui.add_cascade(label="fichier", menu=menu_bar)

window.config(menu=menui)
canva.grid()
window.mainloop()
