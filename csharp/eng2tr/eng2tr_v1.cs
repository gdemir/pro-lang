using System;
using System.IO;

namespace proje1 {
    class KelimeAgaci {
        private string mean;
        KelimeAgaci[] classes = new KelimeAgaci[26];
        char[] alpha = {
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        };
        public KelimeAgaci() {
            mean = "";
        }
        public void KelimeEkle(string key, string value) {
            if (key != "") {
                int index = Array.IndexOf(alpha, key[0]);
                if (classes[index] == null)
                    classes[index] = new KelimeAgaci();
                classes[index].KelimeEkle(key.Substring(1), value);
            } else
                if (mean == "" || mean == "[bu kelime daha onceden silinmis]")
                    mean = value;
                else
                    mean += "; " + value;
        }
        public string AnlamBul(string key) {
            if (key != "") {
                int index = Array.IndexOf(alpha, key[0]);
                if (classes[index] == null)
                    return "[Kelime Bulunamadi]";
                return classes[index].AnlamBul(key.Substring(1));
            } else
                return mean;
        }
        public void KelimeSil(string key) {
            if (key != "") {
                int index = Array.IndexOf(alpha, key[0]);
                classes[index].KelimeSil(key.Substring(1));
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
