import tkinter as tk
from tkinter import messagebox 

def chiffrer_fichier_txt(nom_fichier, cle, ty):
    lignes_modifiees = []

    with open(nom_fichier, "r", encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.rstrip("\n")
            lignes_modifiees.append(chiffrer_cesar(ligne, cle))

    with open(nom_fichier, "w", encoding="utf-8") as f:
        for ligne in lignes_modifiees:
            f.write(ligne + "\n")


def str_to_cle(cle):

    new_cle = 0

    for i in range(len(cle)):
        new_cle = new_cle + ord(cle[i]) - 32

    return new_cle



def chiffrer_cesar(message, cle):   
    
    chiffrer_message = ''

    if type(cle) == str:
        cle = str_to_cle(cle)

    for i in range(len(message)):
        chiffrer_message = chiffrer_message + chr((ord(message[i]) - 32 + cle) % 95 + 32)

    return chiffrer_message
    
def dechiffrer_cesar(message, cle):

    chiffrer_message = ''

    if type(cle) == str:
        cle = str_to_cle(cle)

    for i in range(len(message)):
        chiffrer_message = chiffrer_message + chr((ord(message[i]) - 32 - cle) % 95 + 32)

    return chiffrer_message

# ---------- Fonctions liées à l'interface ----------

def chiffrer_message():
    message = entry_message.get()
    cle = entry_cle.get()

    if message == "" or cle == "":
        messagebox.showerror("Erreur", "Message ou clé manquant")
        return

    resultat = chiffrer_cesar(message, cle)
    label_resultat.config(text="Résultat : " + resultat)


def dechiffrer_message():
    message = entry_message.get()
    cle = entry_cle.get()

    if message == "" or cle == "":
        messagebox.showerror("Erreur", "Message ou clé manquant")
        return

    resultat = dechiffrer_cesar(message, cle)
    label_resultat.config(text="Résultat : " + resultat)


def quitter():
    fenetre.destroy()


# ---------- Fenêtre principale ----------

fenetre = tk.Tk()
fenetre.title("Chiffrement César")
fenetre.geometry("400x300")

# ---------- Widgets ----------

label_message = tk.Label(fenetre, text="Message :")
label_message.pack()

entry_message = tk.Entry(fenetre, width=40)
entry_message.pack()

label_cle = tk.Label(fenetre, text="Clé (nombre ou texte) :")
label_cle.pack()

entry_cle = tk.Entry(fenetre, width=20)
entry_cle.pack()

bouton_chiffrer = tk.Button(fenetre, text="Chiffrer", command=chiffrer_message)
bouton_chiffrer.pack(pady=5)

bouton_dechiffrer = tk.Button(fenetre, text="Déchiffrer", command=dechiffrer_message)
bouton_dechiffrer.pack(pady=5)

bouton_quitter = tk.Button(fenetre, text="Quitter", command=quitter)
bouton_quitter.pack(pady=5)

label_resultat = tk.Label(fenetre, text="Résultat : ")
label_resultat.pack(pady=10)

# ---------- Boucle principale ----------
fenetre.mainloop()