import java.util.Locale;
import java.util.Scanner;

public class Idades {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Locale.setDefault(Locale.US);
		
		String nome1, nome2;
		int idade1, idade2;
		double media;
		
		System.out.println("Dados da primeira pessoa: ");
		System.out.print("Nome: ");
		nome1 = sc.nextLine();
		System.out.print("Idade: ");
		idade1 = sc.nextInt();
		
		System.out.println("Dados da segunda pessoa: ");
		sc.nextLine();
		System.out.print("Nome: ");
		nome2 = sc.nextLine();
		System.out.print("Idade: ");
		idade2 = sc.nextInt();
		
		media = (idade1 + idade2) / 2.0;
		
		System.out.println("A idade media de " + nome1 + " e " + nome2 + " eh de " + String.format("%.1f", media) + " anos");
		
							
		sc.close();
	}
}
