#include <stdio.h>

int     main(void)
{
    int A, cnt, arr[42];

    cnt = 0;
    for (int i=0; i<=41; i++)
    {
        arr[i] = 0;
    }
    for (int i=1; i<=10; i++)
    {
        scanf("%d", &A);
        if (0 <= A && A <= 1000)
        {
            arr[A % 42] += 1;
        }
    }
    for (int i=0; i<=41; i++)
    {
        if (arr[i] != 0)
            cnt++;
    }
    printf("%d\n", cnt);
    return (0);
}