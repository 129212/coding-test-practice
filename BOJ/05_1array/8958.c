#include <stdio.h>
#include <string.h>

int     main(void)
{
    int n, tmp, val, sum;
    char a[80];

    scanf("%d", &n);
    for (int i=0; i<n; i++)
    {
        tmp = 0;
        val = 0;
        scanf("%s", a);
        for (int j=0; j<strlen(a); j++)
        {
            if (a[j] == 'O')
            {
                tmp++;
                val += tmp;
            }
            else if (a[j] == 'X')
                tmp = 0;
        }
        printf("%d\n", val);
    }
}