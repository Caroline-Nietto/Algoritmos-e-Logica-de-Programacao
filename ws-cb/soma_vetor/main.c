#include <stdio.h>
#include <stdlib.h>

int main()
{
   int n;
   double soma, media;

   printf("Quantos numeros voce vai digitar? ");
   scanf("%d", &n);

   double vet[n];
   for (int i = 0; i < n; i++){
    printf("Digite um numero: ");
    scanf("%lf", &vet[i]);
   }

   printf("\n");
   printf("VALORES = ");
   for (int i = 0; i < n; i++){
        printf("%.1lf ", vet[i]);
   }

    soma = 0;
    for (int i = 0; i < n; i++){
        soma = soma + vet[i];
   }

   media = soma / n;

   printf("\nSOMA = %.2lf\n", soma);
   printf("MEDIA = %.2lf\n", media);

    return 0;
}
