using System;
using System.Globalization;

namespace Vetores {
    internal class Program {
        static void Main(string[] args) {

            CultureInfo CI = CultureInfo.InvariantCulture;

            int n;

            Console.Write("Quantos numeros voce vai digitar? ");
            n = int.Parse(Console.ReadLine());

            double[] vet = new double[n];

            for (int i = 0; i < n; i++) {
                Console.Write("Digite um numero: ");
                vet[i] = double.Parse(Console.ReadLine(), CI);
            }
            Console.WriteLine();
            Console.WriteLine("NUMEROS DIGITADOS: ");

            for (int i = 0; i < n; i++) {
                Console.WriteLine(vet[i].ToString("F1", CI));
            }

        }
    }
}