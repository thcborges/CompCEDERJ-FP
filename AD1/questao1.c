#include<stdio.h>
#include<math.h>
int expoente(n,b) {
    int i, e = 1;
    for(i=1;i<=b;i++){
        e*=n;
    }
    return e;
}

int converte(numDecimal, base) {
    int conversao[7], numConvertido = 0, i = 0;
    while (numDecimal > 0) {
        conversao[i] = (numDecimal % base);
        numDecimal /= base;
        i++;
    }
    i--;
    for(i; i >= 0; i--) {
        numConvertido += conversao[i] * expoente(10, i);
    }
    return numConvertido;
}
int main() {
    int numDecimal, i, numConvertido;
    while(scanf("%d", &numDecimal), numDecimal != -1){
        for (i = 2; i < 10; i++) {
            numConvertido = converte(numDecimal, i);
            printf("%d ", numConvertido);
        }
        printf("\n");

    }

    return 0;
}
