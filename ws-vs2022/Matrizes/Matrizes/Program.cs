using System;
using System.Globalization;

namespace Matrizes {
    internal class Program {
        static void Main(string[] args) {

        CultureInfo CI = CultureInfo.InvariantCulture;

            int m, n;

            Console.Write("Quantas linhas vai ter a matriz? ");
            m = int.Parse(Console.ReadLine());
            Console.Write("Quantas colunas vai ter a matriz? ");
            n = int.Parse(Console.ReadLine());

            int[,] mat = new int[m, n];
            
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    Console.Write("Elemento [" + i + "," + j + "] : ");
                    mat[i, j] = int.Parse(Console.ReadLine());
                }
            }
            Console.WriteLine();
            Console.WriteLine("MATRIZ DIGITADA: ");

            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    Console.Write(mat[i, j] + " ");
                }
                Console.WriteLine();
            }
        }
    }
}