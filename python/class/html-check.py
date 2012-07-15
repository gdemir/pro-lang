from stack import Stack
import re
import string

def oku(filename):
	oku = open(filename, "r")
	return "".join(i for i in oku)

def parChecker(filename):
    liste = re.findall("<[/]*\w*>", oku(filename))
    opens = ["<html>", "<body>", "<div>"]
    closers = ["</html>", "</body>", "</div>"]
    s = Stack()

    balanced = True
    index = 0

    while index < len(liste) and balanced:
        symbol = liste[index]
        if symbol in opens:
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.peek()
                if not matches(top, symbol, opens, closers):
                       balanced = False
                else:
                       s.pop()

        index = index + 1

    if balanced and s.isEmpty():
        return True
    else:
        print closers[opens.index(s.pop())], "eksik girdiniz"
        return False

def matches(open, close, opens, closers):
    return opens.index(open) == closers.index(close)

# Test
result = parChecker("index.html")
print "durum : ", result
