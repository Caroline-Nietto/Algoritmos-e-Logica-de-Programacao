#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
    int N, i;

    cout << "Quantos numeros voce vai digitar? ";
    cin >> N;

    double vet[N];

    for (i = 0; i < N; i++)
    {
        cout << "Digite um numero: ";
        cin >> vet[i];
    }

    cout << endl << "NUMEROS DIGITADOS:" << endl;
    cout << fixed << setprecision(1); //definicao de casa decimal
    for (i = 0; i < N; i++) //percorre o vetor
    {
        cout << vet[i] << endl; //pra imprimir na tela
    }
    return 0;
}
