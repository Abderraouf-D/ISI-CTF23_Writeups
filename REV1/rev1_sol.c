#include <stdio.h>
#include <time.h>






int main(){

int i = 0;
for(i ; i<0x27 ; i++){
int enc[37]   = { 0xbc, 0x93, 0x65, 0xbe, 0x57, 0xc5, 0xdd, 0x69, 0x14, 0x5c, 0xdf, 0x98, 0xe4, 0x61, 0x70, 0xf0, 0xdf, 0xe3, 0x75, 0x0d, 0xe7, 0xe7, 0x24, 0x54, 0xab, 0x0d, 0xef, 0xa0, 0xe4, 0xb1, 0x96, 0x63, 0xbc, 0x9b, 0x4b, 0xbb, 0xb5 } ; 

    srand(i) ; 

    int k ;

    for (int j = 0 ; j<i ; j++){
        k=rand();
        enc[j]=enc[j] ^ (k%0xff); 
    }



    for ( int l = 0 ; l< 37 ; l++) printf("%c",enc[l]);
    printf("\n");
}
    return 0  ;
}