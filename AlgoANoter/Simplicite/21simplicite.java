package iut.sae.algo;

public class Algo {

    public static String RLE(String in) {
        // On vérifie si la chaine contient quelque chose pour éviter de dérouler du
        // code inutilement
        if (in == null || in.isEmpty()) {
            return "";
        }
        // On crée un String que l'on va concatener durant l'algo puis retourner
        String resultat = "";
        // On crée 2 char. Ils seront utilisés pour vérifier si la le caractere actuel
        // est toujours le même ou si il a changé. Si il a changé on l'ajoutera au
        // résultat.
        char charPrecedent = in.charAt(0);
        char charCourant;
        // Le nombre de fois qu'un caractère apparait d'affilé. Il s'initialise à 1 et
        // se réinitialise à chaque fois que les 2 char au dessus sont différent.
        int occurences = 1;

        // On va parcourir le String en paramètre comme un tableau, caractère par
        // caractère
        for (int i = 1; i < in.length(); i++) {
            // On met à jour le caractère de l'indice actuel du String.
            charCourant = in.charAt(i);

            if (charPrecedent == charCourant) {
                // Tant que le caratère précédent et celui actuel sont les mêmes on compte.
                occurences++;
            } else {
                // Lorsqu'ils sont différents on ajoute le nombre de fois que le caractère
                // précédent apparait et le caractère dans le String du résultat et on
                // réinitialise le compteur.
                while (occurences > 9) {
                    // Si le caratère apparait plus de 9 fois on entre dans une boucle pour pouvoir
                    // l'insérer plusieurs fois et à chaque fois on diminue le compteur de 9.
                    // On quitte la boucle quand le compteur est inferieur à 9.
                    resultat += "" + 9 + charPrecedent;
                    occurences -= 9;
                }
                resultat += "" + occurences + charPrecedent;
                occurences = 1;
                charPrecedent = charCourant;
            }
        }
        // Lorsqu'on sort de la boucle for il faut insérer le dernier caractère
        while (occurences > 9) {
            resultat += "" + 9 + charPrecedent;
            occurences -= 9;
        }
        resultat += "" + occurences + charPrecedent;

        return resultat;
    }

    public static String RLE(String in, int iteration) throws AlgoException {
        // On lance l'algorithme un nombre de fois égal au nombre d'itération.
        // A chaque itération de la boucle, on donne le String à la fonction et on
        // récupère
        // le résulat que l'on renvoie à nouveau.
        String resultat = in;
        for (int i = 0; i < iteration; i++) {
            resultat = RLE(resultat);
        }
        return resultat;
    }

    public static String unRLE(String in) throws AlgoException {
        // On fait des vérifications avant de lancer l'algorithme pour ne pas le faire
        // tourner pour rien et éviter des erreurs inattendues.
        // La taille de la chaine doit être pair car la chaine est consituée uniquement
        // de paire de valeurs : un nombre d'apparition et un caractère
        if (in == null || in.length() % 2 != 0) {
            throw new AlgoException();
        }
        if (in.isEmpty()) {
            return "";
        }

        String result = "";
        int occurrence;
        char character;

        // On va parcourir la chaine 2 par 2 (on peut se permettre de faire ça car on a
        // déjà vérifié que la chaine est pair)
        for (int i = 0; i < in.length(); i += 2) {
            // -'0' permet de récupérer le char comme un nombre. On part du principe que la
            // chaine est bien une chaine à décoder
            occurrence = in.charAt(i) - '0';
            character = in.charAt(i + 1);
            for (int j = 0; j < occurrence; j++) {
                // On ajoute la lettre dans le résultat un nombre de fois égal au nombre
                // d'occurrence
                result += character;
            }
        }
        return result.toString();
    }

    public static String unRLE(String in, int iteration) throws AlgoException {
        // Ici on a le même principe que pour l'algorithme RLE récursif.
        String result = in;
        for (int i = 0; i < iteration; i++) {
            result = unRLE(result);
        }
        return result;

    }
}
