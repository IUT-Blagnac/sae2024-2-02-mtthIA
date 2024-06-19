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

char *RLE_IT(char *in, int iteration) {
    char * encoded = in;
    for(int i = 0 ; i < iteration; i++){
        encoded = RLE(encoded);
    }
    return encoded;
}

char *unRLE_IT(char *in, int iteration) {
    char * decoded = in;
    for(int i = 0 ; i < iteration; i++){
        decoded = unRLE(decoded);
    }
    return decoded;
}