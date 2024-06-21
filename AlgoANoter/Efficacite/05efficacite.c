#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *RLE(char *in)
{
    char precedent = in[0];
    int compteur = 1;
    int j = 0;
    int len = strlen(in);
    char *rslt = malloc(len*2*sizeof(char));
    for (int i = 1; i <= len; i++)
    {
        if (in[i] != precedent || compteur == 9)
        {
            rslt[j++] = '0' + compteur;
            rslt[j++] = precedent;
            compteur = 0;
            precedent = in[i];
        }
        compteur++;
    }
    return rslt;
}

char *unRLE(char *in)
{
    int len = strlen(in);
    char *rslt = malloc(len*2*sizeof(char));
    int j = 0;
    for (int i = 0; i < len; i+=2){
        int count = in[i] - '0';
        char ch = in[i+1];
        for(int i = 0 ; i < count ; i++){
            rslt[j++] = ch; 
        }
    } 
    return rslt;
}

char *RLERecursif(char *in, int iteration) {
    char * encoded = in;
    for(int i = 0 ; i < iteration; i++){
        encoded = RLE(encoded);
    }
    return encoded;
}

char *unRLERecursif(char *in, int iteration) {
    char * decoded = in;
    for(int i = 0 ; i < iteration; i++){
        decoded = unRLE(decoded);
    }
    return decoded;
}

int main(int argc, char const *argv[])
{
    
printf("Test RLE:\n");
printf("RLE(\"\") = \"%s\"\n", RLE(""));
printf("RLE(\"abc\") = \"%s\"\n", RLE("abc"));
printf("RLE(\"abbccc\") = \"%s\"\n", RLE("abbccc"));
printf("RLE(\"aaabaa\") = \"%s\"\n", RLE("aaabaa"));
printf("RLE(\"aAa\") = \"%s\"\n", RLE("aAa"));
printf("RLE(\"WWWWWWWWWWWWW\") = \"%s\"\n", RLE("WWWWWWWWWWWWW"));



printf("\nTest RLE Recursif:\n");
printf("RLE(\"abc\", 1) = \"%s\"\n", RLERecursif("abc", 1));
printf("RLE(\"abbccc\", 1) = \"%s\"\n", RLERecursif("abbccc", 1));
printf("RLE(\"aaabaa\", 1) = \"%s\"\n", RLERecursif("aaabaa", 1));
printf("RLE(\"aAa\", 1) = \"%s\"\n", RLERecursif("aAa", 1));
printf("RLE(\"abc\", 2) = \"%s\"\n", RLERecursif("abc", 2));
printf("RLE(\"abc\", 3) = \"%s\"\n", RLERecursif("abc", 3));



printf("\nTest unRLE:\n");
printf("unRLE(\"\") = \"%s\"\n", unRLE(""));
printf("unRLE(\"1a1b1c\") = \"%s\"\n", unRLE("1a1b1c"));
printf("unRLE(\"1a2b3c\") = \"%s\"\n", unRLE("1a2b3c"));
printf("unRLE(\"3a1b2a\") = \"%s\"\n", unRLE("3a1b2a"));
printf("unRLE(\"1a1A1a\") = \"%s\"\n", unRLE("1a1A1a"));
printf("unRLE(\"9W4W\") = \"%s\"\n", unRLE("9W4W"));



printf("\nTest unRLE Recursif:\n");
printf("unRLE(\"1a1b1c\", 1) = \"%s\"\n", unRLERecursif("1a1b1c", 1));
printf("unRLE(\"1a2b3c\", 1) = \"%s\"\n", unRLERecursif("1a2b3c", 1));
printf("unRLE(\"3a1b2a\", 1) = \"%s\"\n", unRLERecursif("3a1b2a", 1));
printf("unRLE(\"1a1A1a\", 1) = \"%s\"\n", unRLERecursif("1a1A1a", 1));
printf("unRLE(\"111a111b111c\", 2) = \"%s\"\n", unRLERecursif("111a111b111c", 2));
printf("unRLE(\"311a311b311c\", 3) = \"%s\"\n", unRLERecursif("311a311b311c", 3));



printf("\nTest Perf:\n");
printf("unRLE(RLE(\"SAE\", 60), 60) = \"%s\"\n", unRLERecursif(RLERecursif("SAE", 60), 60));
}





