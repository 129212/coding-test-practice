#include <stdio.h>

int     main(void)
{
    int A, B;

    while (1)
    {
        scanf("%d %d", &A, &B);
        if ((0 < A && A < 10) && (0 < B && B < 10))
        {
            printf("%d\n", A+B);
        }
        else
            return (0);
    }
}