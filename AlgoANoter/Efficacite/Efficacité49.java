package iut.sae.algo;

public class Efficacité {
    public static String RLE(String chaineDeCaractere) {
        if (chaineDeCaractere.length() == 0) {
            return "";
        }

        String resultat = "";
        int compteur = 1;
        char premierCaractere = chaineDeCaractere.charAt(0);

        for (int i = 1; i < chaineDeCaractere.length(); i++) {
            if (chaineDeCaractere.charAt(i) == premierCaractere) {
                compteur++;
                if (compteur == 9) {
                    resultat += compteur + String.valueOf(premierCaractere);
                    compteur = 0;
                }
            } else {
                if (compteur > 0) {
                    resultat += compteur + String.valueOf(premierCaractere);
                }
                premierCaractere = chaineDeCaractere.charAt(i);
                compteur = 1;
            }
        }

        if (compteur > 0) {
            resultat += compteur + String.valueOf(premierCaractere);
        }

        return resultat;
    }

    public static String RLE(String chaineDeCaractere, int iteration) {
        String resultat = chaineDeCaractere;
        for (int i = 0; i < iteration; i++) {
            resultat = RLE(resultat);
        }
        return resultat;
    }

    public static String unRLE(String chaineCompressee) {
        String resultat = "";
        int longueur = chaineCompressee.length();

        for (int i = 0; i < longueur; i++) {
            char caractere = chaineCompressee.charAt(i);

            if (Character.isDigit(caractere)) {
                int nombre = Character.getNumericValue(caractere);
                char caractereSuivant = chaineCompressee.charAt(++i);

                for (int j = 0; j < nombre; j++) {
                    resultat += caractereSuivant;
                }
            } else {
                resultat += caractere;
            }
        }

        return resultat;
    }

    public static String unRLE(String chaineCompressee, int iteration) {
        String resultat = chaineCompressee;
        for (int i = 0; i < iteration; i++) {
            resultat = unRLE(resultat);
        }
        return resultat;
    }

}
