import java.util.Locale;

public class Processamento_Casting_em_Java {

	public static void main(String[] args) {
		
		Locale.setDefault(Locale.US);
		
		double a;
		int b; 
		a = 5.0; 
		b = (int) a; 
		System.out.println(b); 

	}

}
