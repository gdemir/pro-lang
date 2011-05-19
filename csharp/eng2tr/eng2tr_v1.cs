using System;
using System.IO;

namespace proje1 {
    class KelimeAgaci {
        private string mean;
        KelimeAgaci[] nodes = new KelimeAgaci[26];
        public KelimeAgaci() {
            mean = "";
        }
        public void KelimeEkle(string key, string value) {
            if (key != "") {
                int index = key[0] - 'a';
                if (nodes[index] == null)
                    nodes[index] = new KelimeAgaci();
                nodes[index].KelimeEkle(key.Substring(1), value);
            } else
                if (mean == "" || mean == "[bu kelime daha onceden silinmis]") // ikisinide boş olarak gör.
                    mean = value;
                else
                    mean += "; " + value;
        }
        public string AnlamBul(string key) {
            if (key != "") {
                int index = key[0] - 'a';
                if (nodes[index] == null)
                    return "[Kelime Bulunamadi]";
                return nodes[index].AnlamBul(key.Substring(1));
            } else
                return mean;
        }
        public void KelimeSil(string key) {
            if (key != "") {
                int index = key[0] - 'a';
                nodes[index].KelimeSil(key.Substring(1));
            } else
                mean = "[bu kelime daha onceden silinmis]";
        }
    }
    class Program {
        static void Main() {
            KelimeAgaci sozluk = new KelimeAgaci();
            sozluk.KelimeEkle("legal", "yasal");
            sozluk.KelimeEkle("leg", "bacak");
            sozluk.KelimeEkle("a", "bir");
            sozluk.KelimeEkle("legend", "efsane");
            sozluk.KelimeEkle("leg", "dik kenar");
            Console.WriteLine("leg : {0}", sozluk.AnlamBul("leg"));
            Console.WriteLine("bell : {0}", sozluk.AnlamBul("bell"));
            Console.WriteLine("a : {0}", sozluk.AnlamBul("a"));
            Console.WriteLine("legend : {0}", sozluk.AnlamBul("legend"));
            Console.WriteLine("legal : {0}", sozluk.AnlamBul("legal"));
            sozluk.KelimeSil("legal");
            Console.WriteLine("legal : {0}", sozluk.AnlamBul("legal"));
        }
    }
}
