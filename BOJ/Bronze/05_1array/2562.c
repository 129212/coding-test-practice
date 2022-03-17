#include <stdio.h>

int     main(void)
{
    int max, num[9], idx;

    max = 0;
    for (int i=0; i<9; i++)
    {
        scanf("%d", &num[i]);
        if (max < num[i])
        {
            max = num[i];
            idx = i + 1;
        }
    }
    printf("%d\n%d", max, idx);
}