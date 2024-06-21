def RLE(chaine):
  #nombre de fois le caractere
  cpt = 1
  #chaine de sortie compressé
  chaine_rle = ""
  #compteur pour le parcours de la chaine
  i = 0

  #parcours de la chaine
  while i < len(chaine):

    #si on ne sort pas de la chaine et que le caractere est le meme que le suivant 
    if i+1 < len(chaine) and chaine[i] == chaine[i+1]:
      #si le compteur pour une lettre dépasse 9
      if(cpt >= 9):
        #on l'ajoute a la chaine de sortie
        chaine_rle += str(cpt) + chaine[i]
        #on remet le compteur a 0
        cpt = 0
      #on incrémente le compteur du caractere
      cpt += 1
      #on incrémente le compteur pour passer au caractere suivant
      i += 1
    #si on sort de la chaine ou que le caractere est different du suivant alors 
    else:
      #on l'ajoute a la chaine de sortie
      chaine_rle += str(cpt) + chaine[i]
      #on incrémente le compteur pour passer au caractere suivant 
      i+=1
      #on remet le compteur a 1 pour recommencer 
      cpt = 1

  return chaine_rle


def unRLE(chaine):
  #si la chaine est vide ou si le premier caractere n'est pas un chiffre alors la   
  #chaine n'est pas valide 
  if (len(chaine) == 0 or not chaine[0].isdigit()):
    return chaine
  #chaine de sortie décompressé
  chaine_unrle = ""
  #les chiffres sont tous les 2 caracteres donc on avance avec un pas de 2
  for i in range(0,len(chaine)-1, 2):
    #le nombre de fois que le caractere doit etre répété
    cpt = int(chaine[i])
    #la lettre a répéter * le nombre de fois qu'il faut répéter
    chaine_unrle += chaine[i+1] * cpt
  return chaine_unrle


def RLE_recursif(chaine, iteration):
  if(iteration == 0):
    return chaine
  else:
    #on utilise la fonction RLE pour compresser la chaine en fonction du nombre   
    #d'itérations
    return RLE_recursif(RLE(chaine), iteration-1)


def unRLE_recursif(chaine, iteration):
  if(iteration == 0):
    return chaine
  else:
    #on utilise la fonction unRLE pour compresser la chaine en fonction du nombre   
    #d'itérations
    return unRLE_recursif(unRLE(chaine), iteration-1)




