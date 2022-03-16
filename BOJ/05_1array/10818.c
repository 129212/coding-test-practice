#include <stdio.h>

int     main(void)
{
    int N, min, max, i;
    scanf("%d", &N);
    
    int num[N];
    i = 0;
    for (int i=0; i<N; i++)
    {
        scanf("%d", &num[i]);
    }
    min = num[0];
    max = num[0];
    while (i < N)
    {
        if (min > num[i])
            min = num[i];
        if (max < num[i])
            max = num[i];
        i++;
    }
    printf("%d %d\n", min, max);
}