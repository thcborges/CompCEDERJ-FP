#include<stdio.h>
int call(x) {
    if ((x == 0) || (x == 1)) {
        return 1;
    } else {
        return call(x-1) + call(x-2) + 1;
    }
}
int main(){
    int c, i, j, n, x;
    scanf("%d", &n);
    for (i = 0; i < n; i++) {
        scanf("%d", &x);
        int fib1 = 0, fib2 = 1, fibonacci = 0;
        for (j = 1; j < x; j++) {
            fibonacci = fib1 + fib2;
            fib1 = fib2;
            fib2 = fibonacci;
            //printf("j - %d\nfibonacci - %d\n", j, fibonacci);
        }
        c = call(x) - 1;
        printf("fib(%d) = %d calls = %d\n", x, c, fibonacci);
    }
    return 0;
}
