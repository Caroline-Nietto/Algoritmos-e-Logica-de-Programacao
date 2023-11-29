using System;

namespace Diagonal_Negativos {
    internal class Program {
        static void Main(string[] args) {

            int n, cont;

            Console.Write("Qual a ordem da matriz: ");
            n = int.Parse(Console.ReadLine());

            int[,] mat = new int[n, n];

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    Console.Write("Elemento [" + i + "," + j + "]: " );
                    mat[i, j] = int.Parse(Console.ReadLine());
                }
            }

            Console.WriteLine("DIAGONAL PRINCIPAL: ");
            for (int i = 0; i < n; i++) {
                    Console.Write(mat[i, i] + " ");                                
            }

            cont = 0;

            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                   if (mat[i,j] < 0) {
                        cont++;
                    }
                }
            }
            Console.WriteLine();
            Console.WriteLine("QUANTIDADE DE NEGATIVOS = " + cont);

        }
    }
}