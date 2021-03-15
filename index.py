import hashlib
from tkinter import *
from tkinter.messagebox import *
import subprocess

class Password_Checker(Tk):
    """
    The ParentalController Password Checker Class By Div YT#0108
    """
    def __init__(self, idi, password):
        Tk.__init__(self)
        self.title("Password Checker")
        height = 300
        width = 200
        self.geometry(f"{height}x{width}")
        Label(self, text="Identifiant :").place(x=20, y=0)
        self.id = Entry(self, width=25, relief=GROOVE)
        self.id.place(x=20, y=30)
        Label(self, text="Mot de Passe Confidentiel : ").place(x=20, y=60)
        self.motDP = Entry(self, width=25, relief=GROOVE, show="*")
        self.motDP.place(x=20, y=90)
        Button(self, text="Login", command=lambda: self.connect(idi, password), height=2, width=9).place(x=120, y=120)

    def connect(self, idi, password):
        identifiant = hashlib.md5(self.id.get().encode("Utf-8")).hexdigest()
        motdp = hashlib.md5(self.motDP.get().encode("Utf-8")).hexdigest()
        if (identifiant == idi) and (motdp == password):
            self.destroy()
            ParentalControl_Admin().mainloop()

class ParentalControl_Admin(Tk):
    """
    Interface by Div_YT.
    """
    def __init__(self):
        Tk.__init__(self)  # On créée une nouvelle fenetre
        self.title("Interface du Contrôle Parental") #On donne un titre à la fenetre
        height = 400
        width = 250
        self.geometry(f"{height}x{width}")   # On choisit la taille de la fenetre
        self.fen = Frame(self)  # On créée une Frame afin de contenir les widgets
        ## Widgets
        Label(self.fen, text="Temps en secondes : ", font=("Helvetica 11 Bold", 15)).grid(row=0, column=0)
        self.sec = Entry(self.fen, width=25)
        self.sec.grid(row=0, column=1)
        Button(self.fen, text="Programmer\n une fermeture", command=self.programmer).grid(row=1, column=0)
        Button(self.fen, text="Annuler une \n fermeture", command=self.cancel).grid(row=1, column=1)
        ##
        self.fen.grid(row=0, column=0)   # On la pixelise dans la fenetre
        Button(self, text="Quitter sans annuler", command=self.destroy).grid(row=1, column=0)
    
    def cancel(self):
        subprocess.call("shutdown.exe -a")
        showinfo("Arrêt Arrêté", " Nous avons arrêté un arret du système porgrammé. Bonne Journée")

    def programmer(self):
        secondes = self.sec.get()
        subprocess.call(f"""shutdown.exe /s /t {secondes} /c "L'ordinateur va bientôt s'éteindre. Arrêt programmé par {name}""")
        showinfo("Arrêt Programmé", f"Un arrêt a été programmé dans {secondes} secondes.\n Enregistrez vos travaux.")

name = "root"

if __name__ == "__main__":
    idi = hashlib.md5("root".encode("Utf-8")).hexdigest()
    password = hashlib.md5("toor".encode("Utf-8")).hexdigest()
    Password_Checker(idi, password).mainloop()
