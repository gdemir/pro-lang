import string
import time
class F:
	def __init__(self, n):
		self.liste = n

	def show(self):
		u = len(self.liste)
		depo = []
		for c in self.liste:
			depo.append(str(c) + "x^" + str(u))
			u -= 1
		print string.join(depo, " + ")

	def add(self, other):
		if self.liste <= other.liste: uzun, kisa = other.liste, self.liste
		else:						  kisa, uzun = other.liste, self.liste
		son = []
		f = len(uzun) - len(kisa)
		for i in range(f):
			son.append(uzun[i])
		for i in range(len(kisa)):
			son.append(uzun[f] + kisa[i])
			f += 1
		return son

	def div(self, other):
		bolunen = self.liste
		bolen = other.liste
		bolum = []
		while len(bolunen) > len(bolen) or (len(bolunen) == len(bolen) and bolunen[0] > bolen[0]):
			k = bolunen[0] / bolen[0]
			bolum.append(k)
			gecici = [k * c for c in bolen]
			if len(gecici) < len(bolunen):
				u = len(bolunen) - len(gecici)
				for i in range(u):
					gecici.append(0)
			i = 0
			depo = []
			for c in bolunen:
				s = c - gecici[i]
				if s != 0: depo.append(s)
				i += 1
			bolunen = depo
		return bolum

a = F([1, 4, 4])
b = F([1, 2])
a.show()
b.show()
c = a.add(b)
d = a.div(b)
print c, d
