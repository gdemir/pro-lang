using System;
using System.IO;

namespace proje1 {
    class KelimeAgaci {
        public string mean;
        KelimeAgaci[] nodes = new KelimeAgaci[26];
        public KelimeAgaci() {
            mean = "";
        }
        public void KelimeEkle(string key, string value) {
            if (key != "") {
                int index = key[0] - 'a'; // 97
                if (nodes[index] == null)
                    nodes[index] = new KelimeAgaci();
                nodes[index].KelimeEkle(key.Substring(1), value);
            } else
                if (mean == "" || mean == "[bu kelime daha onceden silinmis]") // ikisinide boş olarak gör.
                    mean = value;
                else
                    mean += "; " + value;
        }
        public KelimeAgaci KokBul(KelimeAgaci node, string key) {
            if (key != "") {
                int index = key[0] - 'a'; // 97
                if (nodes[index] == null)
                    return null;
                return nodes[index].KokBul(node, key.Substring(1));
            } else
                return this;
        }
        public string AnlamBul(string key) {
            KelimeAgaci node = KokBul(nodes[key[0] - 'a'], key);
            return (node != null) ? node.mean : "[Kelime Bulunamadi]";
        }
        public void KelimeSil(string key) {
            KelimeAgaci kok = KokBul(nodes[key[0] - 'a'], key);
            if (kok != null)
                kok.mean = "[bu kelime daha onceden silinmis]";
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
