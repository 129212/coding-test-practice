#include <stdio.h>

int     main(void)
{
    int A, B;

    scanf("%d %d", &A, &B);
    if (A > B)
        printf(">\n");
    if (A < B)
        printf("<\n");
    if (A == B)
        printf("==\n");
    return (0);
}