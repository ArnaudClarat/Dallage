#!/usr/bin/python
# coding : UTF-8
import turtle as dessin


def is_number(nbr):
    """
    Fonction qui verifie si un str est un int ou un float
    Source: pythoncentral.io
    :param nbr = String à vérifier:
    :return True ou False:
    """
    try:
        float(nbr)
        return True
    except:
        pass
    if nbr.isdigit():
        return True
    return False


def retry():
    sortie = input("Veuillez réessayer. ")
    return sortie


def carre(cote, long, larg):
    posx = 0
    posy = 0
    dessin.begin_fill()
    for k in range(long):
        for j in range(larg):
            for i in range(4):
                dessin.fd(cote)
                dessin.rt(90)
            posx += cote
        posy += cote


def longueur(long, larg):
    a = 0


def largeur(long, larg):
    a = 0


def main():
    # --- Insertion des données ---
    tailleLa = input("Largeur d'une dalle : ")
    while not is_number(tailleLa):
        tailleLa = retry()
    tailleLon = input("Largeur d'une dalle : ")
    while not is_number(tailleLon):
        tailleLon = retry()
    nbla = input("Nombre de dalle de largeur : ")
    while not is_number(nbla):
        nbla = retry()
    nblo = input("Nombre de dalle en longueur : ")
    while not is_number(nblo):
        nblo = retry()
    tailleLa = int(tailleLa)
    tailleLon = int(tailleLon)
    nbla = int(nbla)
    nblo = int(nblo)

    # --- Utilisation des données ---
    if tailleLon == tailleLa:
        carre(tailleLa, nblo, nbla)
    else:
        lola = input("Dalle placée en longueur ou en largeur? ").upper()
        while lola not in ["LONGUEUR", "LARGEUR"]:
            lola = retry()
        if lola == "LONGUEUR":
            longueur(nbla, nblo)
        else:
            largeur(nbla, nblo)


if __name__ == '__main__':
    main()
