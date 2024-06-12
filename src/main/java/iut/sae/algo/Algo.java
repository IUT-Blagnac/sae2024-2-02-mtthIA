package iut.sae.algo;


public class Algo{
    public static String RLE(String in){
        int cpt = 1;
        StringBuilder chaineRle = new StringBuilder();
        int i=0;

        while(i<in.length()){
            if(i+1 < in.length() && in.charAt(i) == in.charAt(i+1)){
                if(cpt >= 9){
                    chaineRle.append(cpt);
                    chaineRle.append(in.charAt(i));
                    cpt = 0;
                }
                cpt++;
                i++;

            }else{
                chaineRle.append(cpt);
                chaineRle.append(in.charAt(i));
                i++;
                cpt = 1;
            }
        }

        return chaineRle.toString();
    }

    public static String RLE(String in, int iteration) throws AlgoException{
        if(iteration == 0){
            return in;
        }else{
        return RLE(RLE(in), iteration-1);
        }
    }

    public static String unRLE(String in) throws AlgoException{
        if (in.length()==0 || !Character.isDigit(in.charAt(0))){
            return in;
        }
        StringBuilder chaineUnrle = new StringBuilder();
        for(int i = 0; i<in.length(); i+= 2){
            
            int cpt = Character.getNumericValue(in.charAt(i));
            char character = in.charAt(i+1);
            for(int j = 0; j<cpt; j++){
                chaineUnrle.append(character);
            }

        }
        return chaineUnrle.toString();

    }

    public static String unRLE(String in, int iteration) throws AlgoException{
        if(iteration == 0){
            return in;
        }else{
            return unRLE(unRLE(in), iteration-1);
        }

    }
}

