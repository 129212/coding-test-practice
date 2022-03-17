#include <stdio.h>

int     main(void)
{
    int value;

    scanf("%d", &value);
    if ((0 <= value) && (value <= 100))
    {
        if (90 <= value && value <= 100)
            printf("A");
        else if (80 <= value && value < 90)
            printf("B");
        else if (70 <= value && value < 80)
            printf("C");
        else if (60 <= value && value < 70)
            printf("D");
        else
            printf("F");      
    }
    return (0);
}