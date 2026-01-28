import _tkinter

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
