public class Robot {
	int boy;
	int kilo;
	double kx;			/*koordinatx*/
	double ky;			/*koordinaty*/
	double kz;			/*koordinatz*/
	int aci;			/*robot açısı*/
	int MAX;			/*robotun bir hamlede gideceği maximum deger*/
	int isin = 2;  /*robotun ışınlanma hakkı */
	public Robot(int b, int k) {
		boy = b;
		kilo = k;
		MAX = b/4;
		kx = 0;
		ky = 0;
		kz = 0;
		aci = 0;
	}
	void write(String s) {
		System.out.println(s);
	}
	void step(int x, int y) {
		if (select(1, x , y))
			write("bu boydaki robot bu koordinata adım atamaz");
	}
	void rotate(int derece) {
		if (select(2, 360, derece))
			write("robot 360dan fazla dönemez");
	}
	void teleport(int x, int y) {
		if (select(3, x, y))
			write("işinlanmak için güc yok pil bitti,yürüyün pil dolsun");
	}
	void randteleport() {
		int x = (int) Math.random() * 100;
		int y = (int) Math.random() * 100;
		if (select(4, x, y))
			write("işinlanmak için güc yok pil bitti,yürüyün pil dolsun");
	}
	void state() {
		System.out.print("ışın :"+ isin +" boy :"+ boy +" kilo :"+ kilo);
		System.out.println(" aci :"+ aci +" x :"+ kx +" y :"+ ky +" z :"+ kz);
	}
	boolean select(int secenek, int x ,int y) {
		double mesafe = Math.sqrt(Math.pow(x,2) + Math.pow(y,2));
			switch (secenek) {
			case 1: if (MAX >=  mesafe) { kx += x; ky += y; kz += mesafe; isin++;} else return true;
			case 2: if (x >= y && y >= 0)aci += y;else return true;
			case 3: if (isin > 0) { kx = x; ky = y; kz = mesafe; isin--;} else return true;
			case 4: if (isin > 0) {kx = x; ky = y; } else return false;
		}
		return false;
	}
	public static void main(String[] args) {
		Robot k19 = new Robot(180, 75);
		k19.teleport(15, 16);
		k19.state();
		k19.teleport(3, 4);
		k19.state();
		k19.teleport(1, 1);
		k19.state();
		k19.step(3, 4);
		k19.state();
	}
}
