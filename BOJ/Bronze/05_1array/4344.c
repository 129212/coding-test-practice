#include <stdio.h>

int     main(void)
{
    int C, N;
    double sum, cnt, avg;

    scanf("%d", &C);
    for (int i=0; i<C; i++)
    {
        sum = 0;
        avg = 0;
        cnt = 0;
        scanf("%d", &N);
        double val[N];
        val[0] = N;
        for (int j=1; j<=N; j++)
        {
            scanf("%d", &val[j]);
            sum += val[j];
        }
        avg = (double)(sum / N);
        for (int j=1; j<=N; j++)
        {
            if (val[j] > avg)
                cnt++;
        }
        printf("%.3f%%\n", (double)((cnt * 100) / N));
    }
}