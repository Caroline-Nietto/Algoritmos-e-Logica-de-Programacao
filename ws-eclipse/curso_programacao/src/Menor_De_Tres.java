import java.util.Locale;
import java.util.Scanner;

public class Menor_De_Tres {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Locale.setDefault(Locale.US);
		
		int a, b, c, menor;
		
		System.out.print("Primeiro valor: ");
		a = sc.nextInt();
		System.out.print("Segundo valor: ");
		b = sc.nextInt();
		System.out.print("Terceiro valor: ");
		c = sc.nextInt();
		
		if (a < b && a < c) {
			menor = a;
		}	
		else if (b < c) {
			menor = b;
		}	
		else {
			menor = c;
		}
			
		System.out.println("MENOR = " + menor);
		
		sc.close();
	}
}
