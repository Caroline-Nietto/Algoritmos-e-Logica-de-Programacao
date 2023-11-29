#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n, i, j, qtdNegativos;

    printf("Qual a ordem da matriz? ");
    scanf("%d", &n);

    int mat[n][n];

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            printf("Elemento [%d,%d]: ", i, j);
            scanf("%d", &mat[i][j]);
        }
    }

    printf("DIAGONAL PRINCIPAL:\n");

    for (i = 0; i < n; i++)
    {
        printf("%d ", mat[i][i]);
    }

    qtdNegativos = 0;

    for (i = 0; i < n; i++)
    {
        for (j = 0; j < n; j++)
        {
            if (mat[i][j] < 0 )
            {
                qtdNegativos++;
            }
        }
    }
    printf("\nQUANTIDADES DE NEGATIVOS = %d\n", qtdNegativos);

    return 0;
}
