# unRLE

def unRLE(texte_compresse):
    decompresse = ""
    index = 0
    taille = len(texte_compresse)

    while index < taille:
        caractere = texte_compresse[index]
        if caractere.isdigit():
            quantite = int(caractere)
            caractere_suivant = texte_compresse[index + 1]
            decompresse += quantite * caractere_suivant
            index += 2
        else:
            decompresse += caractere
            index += 1
    return decompresse

def unRLE_Recursif(texte_compresse, i):
    result = texte_compresse
    while i > 0:
        result = unRLE(result)
        i -= 1
    return result


# RLE

def RLE(texte):
    compresse = ""
    cpt = 1
    caractere = texte[0]
    taille = len(texte)
    index = 1

    if len(texte) == 0:
        return ""
    while index < taille:
        if texte[index] == caractere:
            cpt += 1
            if cpt == 9:
                compresse += str(cpt) + caractere
                cpt = 0
        else:
            if cpt > 0:
                compresse += str(cpt) + caractere
            caractere = texte[index]
            cpt = 1
        index += 1
    if cpt > 0:
        compresse += str(cpt) + caractere
    return compresse

def RLE_Recursif(texte, i):
    result = texte
    while i > 0:
        result = RLE(result)
        i -= 1
    return result