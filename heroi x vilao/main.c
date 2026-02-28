#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define TF 10
#define Vilao 3

/*
//Prioridades:
    1 -
*/

int posicao(){
    return rand() % TF;
}


void mundo(int x, int y, int x_h, int y_h){ //int h[x][y]
    int i = 0, j = 0;
    for(i = 0; i < TF; i++){
        for(j=0; j < TF; j++){
            if(i == x && j == y){//definindo a posicao do vilao
                printf("[V]");
                continue;
            }
            if(i == x_h && j == y_h){//definindo a posicao do vilao
                printf("[H]");
                continue;
            }
            printf("[ ]");
        }
        printf("\n");
    }
}

void main(){
    srand((unsigned)time(NULL));

    int x = posicao(), y = posicao();
    printf("Vilao: Posicao [%d] [%d]", x, y);

    int x_h = posicao(), y_h = posicao();
    printf("\nHeroi: Posicao [%d] [%d]\n\n", x_h, y_h);

    mundo(x,y,x_h,y_h);

    if(x == x_h && y == y_h){
        printf("\nHeroi com o vilao");
    }else {
        printf("\nHeroi esta longe de vilao");
    }
}
