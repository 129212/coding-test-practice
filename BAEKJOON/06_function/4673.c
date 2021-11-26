#include <stdio.h>

int     *calc_ctor(int n, int limit)
{
    int sum, i, idx, num;
    int temp[50], *ctor;

    i = 0;
    while (n <= limit)
    {
        num = n;
        sum = 0;
        idx = 0;
        temp[0] = 1;
        while (n >= 10)
        {
            temp[idx++] = n % 10;
            n = n / 10;
        }
        temp[idx] = n;
        temp[idx + 1] = -1;
        idx = 0;
        while (temp[idx] >= 0)
        {
            sum += temp[idx++];
        }
        n = sum + num;
        ctor[i++] = n;
    }
    ctor[i] = -1;
    for (int i=0; ctor[i]>0; i++)
    {
        printf("%d\n", ctor[i]);
    }
    return (ctor);
}

int     self_nbr(int n, int limit)
{
    int *ctor, idx;
    int self_nbr[100];

    idx = 0;
    ctor = calc_ctor(n, limit);
    for (int i=1; i<=limit; i++)
    {
        for(int j=0; j<limit; j++)
        {
            if (ctor[j] != i)
            {
                self_nbr[idx++] = i;
            }
        }
    }
    for (int i=0; self_nbr[i]<limit; i++)
    {
        printf(" ---- %d\n", self_nbr[i]);
    }
    return (0);
}

int     main(void)
{
    self_nbr(9900, 10000);

    return (0);
}