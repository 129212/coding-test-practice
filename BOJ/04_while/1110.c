#include <stdio.h>

int main(void)
{
    int N, n1, n2, cycle, nbr;

    scanf("%d", &N);
    nbr = N;
    cycle = 0;
    n1 = 0;
    while ((0 <= N && N <= 99))
    {
        n1 = N % 10;
        n2 = (N / 10) + (N % 10);
        N = (n1 * 10) + (n2 % 10);
        cycle++;
        if (N == nbr)
        {
            printf("%d\n", cycle);
            break;
        }
    }
    return (0);
}