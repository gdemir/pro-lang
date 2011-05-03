import java.util.Scanner;
public class sayitahmini {
	static int al(int deneme,int tahmin,int aranan){
		if (tahmin == aranan){
			System.out.println(deneme+" deneme de buldunuz");
			return 1;
		}
		else{
			if(tahmin > aranan)
				System.out.println("sayiyi azaltiniz");
			else
				System.out.println("sayiyi arttiriniz");
			return 0;
		}
	}	
	public static void main(String[] args) {
		
		Scanner girdi = new Scanner(System.in);
		
		int aranan = (int)(100* Math.random());
		int deneme, tahmin;
		deneme = 0;
		do {
			System.out.println("tahmin ettiginiz sayi?");
			tahmin = girdi.nextInt();
			deneme++;	
		} while(al(deneme,tahmin,aranan) == 0);
	}
}
