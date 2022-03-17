#include <stdio.h>

int     main(void)
{
    int A, B, C;
    int num, check, cnt, len, j;
    int result[50], count[10];

    scanf("%d\n%d\n%d", &A, &B, &C);
    if ((100 <= A && A <= 1000) && (100 <= B && B <= 1000)
        && (100 <= C && C <= 1000))
    {
        num = A * B * C;
        len = 0;
        for (int i=0; num>0; i++)
        {
            result[len++] = num % 10;
            num = num / 10;
        }
        for (int i=0; i<=9; i++)
        {
            cnt = 0;
            for (int j=0; j<len; j++)
            {
                if (i == result[j])
                    cnt++;
            }
            count[i] = cnt;
            printf("%d\n", count[i]);
        }
    }
    return (0);
}