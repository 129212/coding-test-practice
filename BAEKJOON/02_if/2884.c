#include <stdio.h>

int     main(void)
{
    int H, M;
    int newH, newM;

    scanf("%d %d", &H, &M);
    if ((0 <= H && H < 24) && (0 <= M && M < 60))
    {
        if (M < 45)
        {
            if (H == 0)
                newH = (H + 24) - 1;
            else if (H > 0)
                newH = H - 1;
            newM = (M + 60) - 45;
        }
        else if (M >= 45)
        {
            newH = H;
            newM = M - 45;
        }
        printf("%d %d\n", newH, newM);
    }
    return (0);
}