#include <stdio.h>

int     main(void)
{
    int N, X;
    int A;

    scanf("%d %d", &N, &X);
   for (int i=0; i<N; i++)
   {
       scanf("%d", &A);
       if (A < X)
       {
           printf("%d", A);
           printf(" ");
       }
   }
   printf("\n");
}