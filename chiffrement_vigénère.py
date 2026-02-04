import tkinter as tk
from tkinter import messagebox

import os

def chiffrer_fichier_txt(nom_fichier, cle, new_file, mode):
    dossier_source = os.path.dirname(nom_fichier)
    chemin_sortie = os.path.join(dossier_source, new_file)

    lignes_modifiees = []

    with open(nom_fichier, "r", encoding="utf-8") as f:
        for ligne in f:
            ligne = ligne.rstrip("\n")
            if mode == "chiffrer":
                lignes_modifiees.append(chiffrer_vigenere(ligne, cle))
            else:
                lignes_modifiees.append(dechiffrer_vigenere(ligne, cle))

    with open(chemin_sortie, "w", encoding="utf-8") as f:
        for ligne in lignes_modifiees:
            f.write(ligne + "\n")

def chiffrer_vigenere(message, cle):   
    
    chiffrer_message = ''

    for i in range(len(message)):
        
        if ord(message[i]) >= 32 and ord(message[i]) <= 126:
            chiffrer_message = chiffrer_message + chr((ord(message[i]) - 32 + ord(cle[i % len(cle)]) - 32) % 95 + 32)

        else:
            chiffrer_message = chiffrer_message + message[i]

    return chiffrer_message
    
def dechiffrer_vigenere(message, cle):

    chiffrer_message = ''

    for i in range(len(message)):
        
        if ord(message[i]) >= 32 and ord(message[i]) <= 126:
            chiffrer_message = chiffrer_message + chr((ord(message[i]) - 32 - ord(cle[i % len(cle)]) - 32) % 95 + 32)

        else:
            chiffrer_message = chiffrer_message + message[i]

    return chiffrer_message

# ---------- Fonctions liées à l'interface ----------

def chiffrer_message():
    message = entry_message.get()
    cle = entry_cle.get()

    if message == "" or cle == "":
        messagebox.showerror("Erreur", "Message ou clé manquant")
        return

    resultat = chiffrer_vigenere(message, cle)
    label_resultat.config(text="Résultat : " + resultat)


def dechiffrer_message():
    message = entry_message.get()
    cle = entry_cle.get()

    if message == "" or cle == "":
        messagebox.showerror("Erreur", "Message ou clé manquant")
        return

    resultat = dechiffrer_vigenere(message, cle)
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

# chiffrer_fichier_txt(r"C:\Users\nosty\OneDrive\Bureau\Algo\The Dunwich Horror.txt", "~lelou%C'oPslsx)f~:-ru7={", "The Dunwich Horror_q1.txt", "chiffrer")
# chiffrer_fichier_txt(r"C:\Users\nosty\OneDrive\Bureau\Algo\The Call of Cthulhu.txt", "The Call of Cthulhu.txt", "The Dunwich Horror_q2.txt", "chiffrer")