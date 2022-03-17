#include <stdio.h>

int     main(void)
{
    int A, B;

    while (scanf("%d %d", &A, &B) != EOF)
    {
        if ((0 < A && A < 10) && (0 < B && B < 10))
        {
            printf("%d\n", A+B);
        }
        else
            return (0);
    }
}