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

def unRLERecursif(texte_compresse, i):
    result = texte_compresse
    while i > 0:
        result = unRLE(result)
        i -= 1
    return result


# RLE

def RLE(texte):
    if len(texte) == 0:
        return ""
    compresse = ""
    cpt = 1
    caractere = texte[0]
    taille = len(texte)
    index = 1

    
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

def RLERecursif(texte, i):
    result = texte
    while i > 0:
        result = RLE(result)
        i -= 1
    return result

print("Test RLE:")
print('RLE("") = "{}"'.format(RLE("")))
print('RLE("abc") = "{}"'.format(RLE("abc")))
print('RLE("abbccc") = "{}"'.format(RLE("abbccc")))
print('RLE("aaabaa") = "{}"'.format(RLE("aaabaa")))
print('RLE("aAa") = "{}"'.format(RLE("aAa")))
print('RLE("WWWWWWWWWWWWW") = "{}"'.format(RLE("WWWWWWWWWWWWW")))

print("\nTest RLE Recursif:")
print('RLE("abc", 1) = "{}"'.format(RLERecursif("abc", 1)))
print('RLE("abbccc", 1) = "{}"'.format(RLERecursif("abbccc", 1)))
print('RLE("aaabaa", 1) = "{}"'.format(RLERecursif("aaabaa", 1)))
print('RLE("aAa", 1) = "{}"'.format(RLERecursif("aAa", 1)))
print('RLE("abc", 2) = "{}"'.format(RLERecursif("abc", 2)))
print('RLE("abc", 3) = "{}"'.format(RLERecursif("abc", 3)))

print("\nTest unRLE:")
print('unRLE("") = "{}"'.format(unRLE("")))
print('unRLE("1a1b1c") = "{}"'.format(unRLE("1a1b1c")))
print('unRLE("1a2b3c") = "{}"'.format(unRLE("1a2b3c")))
print('unRLE("3a1b2a") = "{}"'.format(unRLE("3a1b2a")))
print('unRLE("1a1A1a") = "{}"'.format(unRLE("1a1A1a")))
print('unRLE("9W4W") = "{}"'.format(unRLE("9W4W")))
print(unRLE("aaabbb"))

print("\nTest unRLE Recursif:")
print('unRLE("1a1b1c", 1) = "{}"'.format(unRLERecursif("1a1b1c", 1)))
print('unRLE("1a2b3c", 1) = "{}"'.format(unRLERecursif("1a2b3c", 1)))
print('unRLE("3a1b2a", 1) = "{}"'.format(unRLERecursif("3a1b2a", 1)))
print('unRLE("1a1A1a", 1) = "{}"'.format(unRLERecursif("1a1A1a", 1)))
print('unRLE("111a111b111c", 2) = "{}"'.format(unRLERecursif("111a111b111c", 2)))
print('unRLE("311a311b311c", 3) = "{}"'.format(unRLERecursif("311a311b311c", 3)))

print("\nTest Perf:")
print('unRLE(RLE("SAE", 60), 60) = "{}"'.format(unRLERecursif(RLERecursif("SAE", 30), 30)))
