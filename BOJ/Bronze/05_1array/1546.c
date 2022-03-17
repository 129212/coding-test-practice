#include <stdio.h>

int     main(void)
{
    int N;
    double M, sum;

    M = 0;
    sum = 0;
    scanf("%d", &N);
    double val[N];
    for (int i=0; i<N; i++)
    {
        scanf("%lf", &(val[i]));
        if (M < val[i])
            M = val[i];
    }
    for (int i=0; i<N; i++)
    {
        val[i] = (val[i] *100) / M;
        sum += val[i];
    }
    printf("%lf\n", sum / (double)N);
}