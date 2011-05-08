using System;
using System.IO;

namespace proje1 {
	class ReadWrite {
	        public static string read(string file) {
			string okunan = "";
			StreamReader oku = new StreamReader(file);
			okunan = oku.ReadToEnd();
			oku.Close();
			return okunan;
		}
	}
	class Stack {
		private string[] items;
		private int index;
		public Stack(int N) {
			items = new string[N];
			index = -1;
		}
		public bool IsEmpty() {
			return index == -1;
		}
		public int Push(string item) {
			if (items[items.Length - 1] != null)
				return -1;
			else {
				items[++index] = item;
				return index;
			}
		}
		public string Pop() {
			if (IsEmpty())
				return null;
			else {
				string item = items[index];
				items[index--] = null;
				return item;
			}
		}
		public string Peek() {
			if (IsEmpty())
				return null;
			else
				return items[index];
		}
	}
	class StrOperation {
		public static string bold(string str) {
			int i;
			string temp = "";
			for (i = 0; i < str.Length; i++)
				temp = temp + str[i] + str[i];
			return temp;
		}
		public static string upper(string str) {
			return str.ToUpper();
		}
		public static string hide(string str) {
			return "";
		}
		public static string paragraph(string str) {
			return String.Concat("[", str, "]");
		}
	}
	class Tag2Text {
		private static string operation(string tag, string str) {
			string[] tags = {"<u>", "<b>", "<h>", "<p>"},
				 funcs = {StrOperation.upper(str), StrOperation.bold(str), StrOperation.hide(str), StrOperation.paragraph(str)};
			return funcs[Array.IndexOf(tags, tag)];
		}
		private static bool balance(string open, string close) {
			string[] opens = {"<u>", "<b>", "<h>", "<p>"},
				 closes = {"</u>", "</b>", "</h>", "</p>"};
			return Array.IndexOf(opens, open) == Array.IndexOf(closes, close);
		}
		public static string process(string s) {
			Stack tags = new Stack(100),
			      temp = new Stack(100);
			string tag = "",
			       word = "",
			       result = "";
			bool state = false;
			int i;
			for (i = 0; i < s.Length; i++) {
				if (s[i] == '<') {
					state = true;
					if (word != "") {
						while ((tag = tags.Pop()) != null) {
							word = operation(tag, word);
							temp.Push(tag);
						}
						while ((tag = temp.Pop()) != null)
							tags.Push(tag);
						result += word;
					}
					word = "";
					tag += s[i];
				} else if (state && s[i] == '>') {
					tag += s[i];
					if (tag[1] == '/') {
						if (tags.IsEmpty()) // >pop yapıyorsun ama stack boş.
							return "";
						if (balance(tags.Peek(), tag)) {
							tags.Pop();
						} else // >pop yapılan elaman ile özdeş değil.
							return "";
					} else
						tags.Push(tag);
					tag = "";
					state = false;
				} else if (state)
					tag += s[i];
				else
					word += s[i];
			}
			result += word;
			if (!tags.IsEmpty()) // >hala item var o yüzden hatalı.
				return "";
			return result;
		}
	}
	class Program {
		static void Main() {
			string str = ReadWrite.read("t1.txt");
			string result;
			if ((result = Tag2Text.process(str)) != "")
				Console.WriteLine("{0}", result);
			else
				Console.WriteLine("Kaynak dosyanin bicimleme etiketleri hatalidir, kontrol ediniz.");
		}
	}
}
