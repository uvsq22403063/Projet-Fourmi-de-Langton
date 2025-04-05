import tkinter as tk
import subprocess


window = tk.Tk()
window.title("La Fourmi de Langton")
window.config(bg="#0a0a0a")


def openning():

    subprocess.run(["python", ".\\test\\quadrillage_mieux.py"])

    return


bouton = tk.Button(window, text="ouvrir", command=openning)


bouton.grid()
window.mainloop()
