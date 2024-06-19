

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *RLE(char *in)
{
    char precedent = in[0];
    int compteur = 1;
    int j = 0;
    int len = strlen(in);
    char *rslt = malloc((j)*sizeof(char));
    for (int i = 1; i <= len; i++)
    {
        if (in[i] != precedent || compteur == 9)
        {
            rslt = realloc(rslt, (j+2)*sizeof(char));
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
            rslt = realloc(rslt, (j+1)*sizeof(char));
            rslt[j++] = ch; 
        }
    } 
    rslt[j] = '\0'; 
    return rslt;
}

char *RLE_IT(char *in, int iteration) {
    char * encoded = strdup(in);
    for(int i = 0 ; i < iteration; i++){
        char * tmp = RLE(encoded);
        free(encoded);
        encoded = tmp;
    }
    return encoded;
}

char *unRLE_IT(char *in, int iteration) {
    char * decoded = strdup(in);
    for(int i = 0 ; i < iteration; i++){
        char *tmp = unRLE(decoded);
        free(decoded);
        decoded = tmp;
    }
    return decoded;
}



int main(void)
{
    printf("%s\n", RLE("abc"));
    printf("%s\n", unRLE("1D5B6A"));
    
    printf("%s\n", RLE_IT("abc", 2));
    printf("%s\n", unRLE_IT("111a111b111c", 2));
}