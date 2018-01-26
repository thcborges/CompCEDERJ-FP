#include<stdio.h>
bool verificaPalindromo(expressao){

}
int main() {
    char expressao[100];
    while(scanf("%s", &expressao), expressao != fim){
        if(verifcaPalindromo(expressao)) {
            printf("é palíndromo\n");
        } else {
            printf("não é palíndromo\n")
        }
    }
}
