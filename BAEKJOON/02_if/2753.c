#include <stdio.h>

int     main(void)
{
    int num;

    scanf("%d", &num);
    if (1 <= num && num <= 4000)
    {
        if ((num % 4 == 0) && (num % 100 != 0 || num % 400 == 0))
            printf("1\n");
        else 
            printf("0\n");
    }
    return (0);
}