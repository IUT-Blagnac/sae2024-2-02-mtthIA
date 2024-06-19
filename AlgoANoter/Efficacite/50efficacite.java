//package iut.sae.algo;

public class efficacite{
    public static String RLE(String in){
        int finChaine = in.length();
        String resultat = "";
            for (int i = 0; i < finChaine; i++){
                char lettre = in.charAt(i);
                int cpt = 1;
                while (i + 1 < finChaine && in.charAt(i + 1) == lettre){
                    i++;
                    cpt++;
                }
                if (cpt > 9){
                    resultat = resultat + "9" + lettre + (cpt - 9) + lettre;
                } else {
                    resultat = resultat + cpt + "" + lettre;
                }
            }
            return resultat;
    }

    public static String RLE(String in, int iteration) throws AlgoException{
        if (iteration == 1){
            return RLE(in);
        } else {
            return RLE(RLE(in, iteration - 1));
        }
    }

    public static String unRLE(String in) throws AlgoException{
        int finChaine = in.length();
        String resultat = "";
        for (int i = 0; i < finChaine; i++){
            char lettre = in.charAt(i);
            if (Character.isDigit(lettre)){
                int cpt = Character.getNumericValue(lettre);
                lettre = in.charAt(i + 1);
                for (int j = 0; j < cpt; j++){
                    resultat = resultat + lettre;
                }
                i++;
            } else {
                resultat = resultat + lettre;
            }
        }
        return resultat;
    }

    public static String unRLE(String in, int iteration) throws AlgoException{
        if (iteration == 1){
            return unRLE(in);
        } else {
            return unRLE(unRLE(in, iteration - 1));
        }
    }
}

