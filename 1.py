#Король	K/k

#Ферзь	Q/q
#Ладья	R/r
#Слон	B/b
#Конь	N/n
#Пешка	P/p	

class Figure:
	def __init__(self, name, col, p, doska, r='  ABCDEFGH  '):
		self.name = name
		self.col = col
		self.p1 = p[:2]
		self.p2 = p[3:5]
		self.p3 = p[6:]
		self.doska = doska
		self.r = r 
		
		
		
class Doska(Figure):
	def __init__(self, name='', col='', p='', doska='', r='  ABCDEFGH  '):
		Figure.__init__(self, name, col, p, doska, r='  ABCDEFGH  ')
	def vavod(self):
		print('-----------------------')
		print('|   A B C D E F G H   |')
		print('|                     |')
		i = 8
		for x in self.doska:
			print('|', i, *x, i, '|')
			i -=1
		print('|                     |')
		print('|   A B C D E F G H   |')
		print('-----------------------')
		return ''
	def hodnazad(self, hn):
		if hn=='':
			print('Нельзя больше сделать ход назад')
			return False
		w1 = hn[-6:-4]
		w11 = hn[-4]
		w2 = hn[-3:-1]
		w22 = hn[-1]					
		self.doska[8 - int(w1[1])][self.r.find(w1[0])-2] = w11
		self.doska[8 - int(w2[-1])][r.find(w2[-2])-2] = w22
		hn = hn[:-6]
		return True		
	def hod(self, hn):
		if self.p1 + self.p2 == 'НААД':
			return self.hodnazad(hn)
		else:
			kl = d.doska[8 - int(p[1])][r.find(p[0])-2]
			if kl == 'K' or kl == 'k':
				f = Korol(kl, col, p, d.doska)
			elif kl == 'Q' or kl == 'q':
				f = Ferz(kl, col, p, d.doska)
			elif kl == 'R' or kl == 'r':
				f = Ladiy(kl, col, p, d.doska)
			elif kl == 'B' or kl == 'b':
				f = Slon(kl, col, p, d.doska)
			elif kl == 'N' or kl == 'n':
				f = Kon(kl, col, p, d.doska)
			elif kl == 'P' or kl == 'p':
				f = Peshka(kl, col, p, d.doska)
			elif kl == 'S' or kl == 's':
				f = Son(kl, col, p, d.doska)
			elif kl == 'O' or kl == 'o':
				f = Odnadiagonali(kl, col, p, d.doska)
			elif kl == 'D' or kl == 'd':
				f = Dvediagonali(kl, col, p, d.doska)
			elif kl == 'A' or kl == 'a':
				f = Сhecke(kl, col, p, d.doska)
			return f.proverka()
	def provkor(self):
		vK = False
		vk = False
		for x in d.doska:
			if "K" in x:
				vK = True
			if "k" in x:
				vk = True
		return vk and vK
	def cooll(self, i):
		if i % 2 == 0:
			col = 'b'
			print('ходят черные')
		else:
			col = 'w'
			print('ходят белые')
		return col

class Peshka(Doska):
	def __init__(self, name, col, p, doska, r='  ABCDEFGH  '):
		Doska.__init__(self, name, col, p, doska, r='  ABCDEFGH  ')
	def proverka(self):
		a1 = 0
		ar = 0
		al = 0
		a2 = 0
		tr = ''
		tl = ''
		if self.col == 'w':
			if self.name == 'P':
				if (self.p1[1] == '2'):
					a1 = 1
					self.doska[8 - int(self.p1[1])-1][self.r.find(self.p1[0])-2] = '*'
					self.doska[8 - int(self.p1[1])-2][self.r.find(self.p1[0])-2] = '*'
				if self.doska[8 - int(self.p1[1])-1][self.r.find(self.p1[0])-2+1] != '.':
					ar = 1
					tr = self.doska[8 - int(self.p1[1])-1][self.r.find(self.p1[0])-2+1]
					self.doska[8 - int(self.p1[1])-1][self.r.find(self.p1[0])-2+1] = '*'
				if self.doska[8 - int(self.p1[1])-1][self.r.find(self.p1[0])-2-1] != '.':
					al = 1
					tl =  self.doska[8 - int(self.p1[1])-1][self.r.find(self.p1[0])-2-1]
					self.doska[8 - int(self.p1[1])-1][self.r.find(self.p1[0])-2-1] = '*'
				if self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2+1] == '.':
					a2 = 1
					self.doska[8 - int(self.p1[1])-1][self.r.find(self.p1[0])-2] = '*'
				self.vavod()
				if a1 == 1:
					self.doska[8 - int(self.p1[1])-1][self.r.find(self.p1[0])-2] = '.'
					self.doska[8 - int(self.p1[1])-2][self.r.find(self.p1[0])-2] = '.'
				if ar == 1:
					self.doska[8 - int(self.p1[1])-1][self.r.find(self.p1[0])-2+1] = tr
				if al == 1:
					self.doska[8 - int(self.p1[1])-1][self.r.find(self.p1[0])-2-1] = tl
				if a2 == 1:
					self.doska[8 - int(self.p1[1])-1][self.r.find(self.p1[0])-2] = '.'

					
						
				
				
				
				if (int(self.p1[1]) + 2 == int(self.p2[1])):
					if (self.p1[1] == '2'):
						if self.doska[8 - int(self.p2[1])][r.find(self.p2[0])-2] == '.':
							self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
							self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2] = '.'
							return True
				elif (int(self.p1[1]) + 1 == int(self.p2[1])) and ((self.r.find(self.p1[0]) + 1 == self.r.find(self.p2[0])) or (self.r.find(self.p1[0]) - 1 == self.r.find(self.p2[0]))):		
					if self.doska[8 - int(self.p2[1])][self.r.find(self.p2[0])-2] != '.':
						self.doska[8 - int(self.p2[-1])][self.r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
						self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2] = '.'
						return True
				elif (int(self.p1[1]) + 1 == int(self.p2[1])):
					if self.doska[8 - int(self.p2[1])][self.r.find(self.p2[0])-2] == '.':
						self.doska[8 - int(self.p2[-1])][self.r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
						self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2] = '.'
						return True

			
			
		elif self.col == 'b':
			if self.name == 'p':
				
				if (self.p1[1] == '7'):
					a1 = 1
					self.doska[8 - int(self.p1[1])+1][self.r.find(self.p1[0])-2] = '*'
					self.doska[8 - int(self.p1[1])+2][self.r.find(self.p1[0])-2] = '*'
				if self.doska[8 - int(self.p1[1])+1][self.r.find(self.p1[0])-2-1] != '.':
					ar = 1
					tr = self.doska[8 - int(self.p1[1])+1][self.r.find(self.p1[0])-2-1]
					self.doska[8 - int(self.p1[1])+1][self.r.find(self.p1[0])-2-1] = '*'
				if self.doska[8 - int(self.p1[1])+1][self.r.find(self.p1[0])-2+1] != '.':
					al = 1
					tl =  self.doska[8 - int(self.p1[1])+1][self.r.find(self.p1[0])-2+1]
					self.doska[8 - int(self.p1[1])+1][self.r.find(self.p1[0])-2+1] = '*'
				if self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2-1] == '.':
					a2 = 1
					self.doska[8 - int(self.p1[1])+1][self.r.find(self.p1[0])-2] = '*'
				self.vavod()
				if a1 == 1:
					self.doska[8 - int(self.p1[1])+1][self.r.find(self.p1[0])-2] = '.'
					self.doska[8 - int(self.p1[1])+2][self.r.find(self.p1[0])-2] = '.'
				if ar == 1:
					self.doska[8 - int(self.p1[1])+1][self.r.find(self.p1[0])-2-1] = tr
				if al == 1:
					self.doska[8 - int(self.p1[1])+1][self.r.find(self.p1[0])-2+1] = tl
				if a2 == 1:
					self.doska[8 - int(self.p1[1])+1][self.r.find(self.p1[0])-2] = '.'


				
				
				if (int(self.p1[1]) - 2 == int(self.p2[1])):
					if (self.p1[1] == '7'):
						if self.doska[8 - int(self.p2[1])][r.find(self.p2[0])-2] == '.':
							self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
							self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2] = '.'
							return True
				elif (int(self.p1[1]) - 1 == int(self.p2[1])) and ((self.r.find(self.p1[0]) + 1 == self.r.find(self.p2[0])) or (self.r.find(self.p1[0]) - 1 == self.r.find(self.p2[0]))):		
					if self.doska[8 - int(self.p2[1])][self.r.find(self.p2[0])-2] != '.':
						self.doska[8 - int(self.p2[-1])][self.r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
						self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2] = '.'
						return True
				elif (int(self.p1[1]) - 1 == int(self.p2[1])):
					if self.doska[8 - int(self.p2[1])][self.r.find(self.p2[0])-2] == '.':
						self.doska[8 - int(self.p2[-1])][self.r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
						self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2] = '.'
						return True
		return False
		

class Kon(Doska):
	def __init__(self, name, col, p, doska, r='  ABCDEFGH  '):
		Doska.__init__(self, name, col, p, doska, r='  ABCDEFGH  ')
	def proverka(self):
		if self.col == 'w' and self.name == 'N':
			y = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', 'p', '.']
		elif self.col == 'b' and self.name == 'n':
			y = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P', '.'] 	
		else:
			return False
		a1 = 0
		a2 = 0
		a3 = 0
		a4 = 0
		a5 = 0
		a6 = 0
		a7 = 0
		a8 = 0
		h2 = ''
		h3 = ''
		h4 = ''
		h5 = ''
		h6 = ''
		h7 = ''
		h8 = ''
		t1 = 8 - int(self.p1[1]) 
		t2 = self.r.find(self.p1[0])-2
		if t1 + 2 < 8 and t1 + 2 >= 0 and t2 + 1 < 8 and t2 + 1 >= 0 and self.doska[t1+2][t2+1] in y:
			a1 = 1
			h1 = self.doska[t1+2][t2+1]
			self.doska[t1+2][t2+1] = '*'
		if t1 + 2 < 8 and t1 + 2 >= 0 and t2 - 1 < 8 and t2 - 1 >= 0 and self.doska[t1+2][t2-1] in y:
			a2 = 1
			h2 = self.doska[t1+2][t2-1]
			self.doska[t1+2][t2-1] = '*'
		if t1 - 2 < 8 and t1 - 2 >= 0 and t2 + 1 < 8 and t2 + 1 >= 0 and self.doska[t1-2][t2+1] in y:
			a3 = 1
			h3 = self.doska[t1-2][t2+1]
			self.doska[t1-2][t2+1] = '*'
		if t1 - 2 < 8 and t1 - 2 >= 0 and t2 - 1 < 8 and t2 - 1 >= 0 and self.doska[t1-2][t2-1] in y:
			a4 = 1
			h4 = self.doska[t1-2][t2-1]
			self.doska[t1-2][t2-1] = '*'
		if t1 + 1 < 8 and t1 + 1 >= 0 and t2 + 2 < 8 and t2 + 2 >= 0 and self.doska[t1+1][t2+2] in y:
			a5 = 1
			h5 = self.doska[t1+1][t2+2]
			self.doska[t1+1][t2+2] = '*'
		if t1 + 1 < 8 and t1 + 1 >= 0 and t2 - 2 < 8 and t2 - 2 >= 0 and self.doska[t1+1][t2-2] in y:
			a6 = 1
			h6 = self.doska[t1+1][t2-2]
			self.doska[t1+1][t2-2] = '*'
		if t1 - 1 < 8 and t1 - 1 >= 0 and t2 + 2 < 8 and t2 + 2 >= 0 and self.doska[t1-1][t2+2] in y:
			a7 = 1
			h7 = self.doska[t1-1][t2+2]
			self.doska[t1-1][t2+2] = '*'
		if t1 - 1 < 8 and t1 - 1 >= 0 and t2 - 2 < 8 and t2 - 2 >= 0 and self.doska[t1-1][t2-2] in y:
			a8 = 1
			h8 = self.doska[t1-1][t2-2]
			self.doska[t1-1][t2-2] = '*'
		self.vavod()
		
		if a1 == 1:
			self.doska[t1+2][t2+1] = h1
		if a2 == 1:
			self.doska[t1+2][t2-1] = h2
		if a3 == 1:
			self.doska[t1-2][t2+1] = h3
		if a4 == 1:
			self.doska[t1-2][t2-1] = h4
		if a5 == 1:
			self.doska[t1+1][t2+2] = h5
		if a6 == 1:
			self.doska[t1+1][t2-2] = h6
		if a7 == 1:
			self.doska[t1-1][t2+2] = h7
		if a8 == 1:
			self.doska[t1-1][t2-2] = h8
		
		
		if (self.col == 'w' and self.name == 'N') or (self.col == 'b' and self.name == 'n'):
			if (int(self.p1[1]) + 2 == int(self.p2[1]) or int(self.p1[1]) - 2 == int(self.p2[1])):
				if ((self.r.find(self.p1[0]) + 1 == self.r.find(self.p2[0])) or (self.r.find(self.p1[0]) - 1 == self.r.find(self.p2[0]))):
					self.doska[8 - int(self.p2[-1])][self.r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
					self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2] = '.'
					return True
			elif (int(self.p1[1]) + 1 == int(self.p2[1]) or int(self.p1[1]) - 1 == int(self.p2[1])):
				if ((self.r.find(self.p1[0]) + 2 == self.r.find(self.p2[0])) or (self.r.find(self.p1[0]) - 2 == self.r.find(self.p2[0]))):
					self.doska[8 - int(self.p2[-1])][self.r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
					self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2] = '.'
					return True
		return False
			


class Slon(Doska):
	def __init__(self, name, col, p, doska, r='  ABCDEFGH  '):
		Doska.__init__(self, name, col, p, doska, r='  ABCDEFGH  ')
	def proverka(self):
		if self.col == 'w' and self.name == 'B':
			y = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', 'p', '.']
		elif self.col == 'b' and self.name == 'b':
			y = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P', '.'] 	
		else:
			return False
		
		
		a1 = {}
		h1 = {}
		a2 = {}
		h2 = {}
		a3 = {}
		h3 = {}
		a4 = {}
		h4 = {}
			
		
		t1 = 8 - int(self.p1[1]) 
		t2 = self.r.find(self.p1[0])-2
		for x in range(1, 8):
			if t1 + x < 8 and t1 + x >= 0 and t2 + x < 8 and t2 + x >= 0 and self.doska[t1+x][t2+x] in y and ((x != 1 and a1[x-1] == 1) or (x == 1)):
				a1[x] = 1
				h1[x] = self.doska[t1+x][t2+x]
				self.doska[t1+x][t2+x] = '*'
			else:
				a1[x] = 0
		for x in range(1, 8):
			if t1 - x < 8 and t1 - x >= 0 and t2 + x < 8 and t2 + x >= 0 and self.doska[t1-x][t2+x] in y and ((x != 1 and a2[x-1] == 1) or (x == 1)):
				a2[x] = 1
				h2[x] = self.doska[t1-x][t2+x]
				self.doska[t1-x][t2+x] = '*'
			else:
				a2[x] = 0
		for x in range(1, 8):
			if t1 + x < 8 and t1 + x >= 0 and t2 - x < 8 and t2 - x >= 0 and self.doska[t1+x][t2-x] in y and ((x != 1 and a3[x-1] == 1) or (x == 1)):
				a3[x] = 1
				h3[x] = self.doska[t1+x][t2-x]
				self.doska[t1+x][t2-x] = '*'
			else:
				a3[x] = 0
		for x in range(1, 8):
			if t1 - x < 8 and t1 - x >= 0 and t2 - x < 8 and t2 - x >= 0 and self.doska[t1-x][t2-x] in y and ((x != 1 and a4[x-1] == 1) or (x == 1)):
				a4[x] = 1
				h4[x] = self.doska[t1-x][t2-x]
				self.doska[t1-x][t2-x] = '*'
			else:
				a4[x] = 0
		self.vavod()
		for x in range(1, 8):
			if a1[x] == 1:
				self.doska[t1+x][t2+x] = h1[x]
		for x in range(1, 8):
			if a2[x] == 1:
				self.doska[t1-x][t2+x] = h2[x]
		for x in range(1, 8):
			if a3[x] == 1:
				self.doska[t1+x][t2-x] = h3[x]
		for x in range(1, 8):
			if a4[x] == 1:
				self.doska[t1-x][t2-x] = h4[x]
		
		if self.col == 'w' and self.name == 'B':
			y = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', 'p']
		elif self.col == 'b' and self.name == 'b':
			y = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P'] 	
		else:
			return False
		if abs(self.r.find(self.p1[0]) - self.r.find(self.p2[0])) == abs(int(self.p1[1]) - int(self.p2[1])):
			q = abs(int(self.p1[1]) - int(self.p2[1]))
			m2 = 1 if (self.r.find(self.p1[0]) - self.r.find(self.p2[0])) < 0 else -1
			m1 = 1 if (int(self.p1[1]) - int(self.p2[1])) < 0 else -1
			e = ''
			z2 = self.r.find(self.p1[0])-2
			z1 = int(self.p1[1])
			for x in range(q):
				z1 += m1
				z2 += m2
				e += self.doska[8-z1][z2]
			if (e.count('.') == q) or ((e.count('.') == q-1 and e[-1] in y)):
				self.doska[8 - int(self.p2[-1])][self.r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
				self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2] = '.'
				return True
		return False
		
class Ladiy(Doska):
	def __init__(self, name, col, p, doska, r='  ABCDEFGH  '):
		Doska.__init__(self, name, col, p, doska, r='  ABCDEFGH  ')
	def proverka(self):
		if self.col == 'w' and self.name == 'R':
			y = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', 'p', '.']
		elif self.col == 'b' and self.name == 'r':
			y = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P', '.'] 	
		else:
			return False
		
		
		a1 = {}
		h1 = {}
		a2 = {}
		h2 = {}
		a3 = {}
		h3 = {}
		a4 = {}
		h4 = {}
			
		
		t1 = 8 - int(self.p1[1]) 
		t2 = self.r.find(self.p1[0])-2
		for x in range(1, 8):
			if t1 + x < 8 and t1 + x >= 0 and self.doska[t1+x][t2] in y and ((x != 1 and a1[x-1] == 1) or (x == 1)):
				a1[x] = 1
				h1[x] = self.doska[t1+x][t2]
				self.doska[t1+x][t2] = '*'
			else:
				a1[x] = 0
		for x in range(1, 8):
			if t1 - x < 8 and t1 - x >= 0 and self.doska[t1-x][t2] in y and ((x != 1 and a2[x-1] == 1) or (x == 1)):
				a2[x] = 1
				h2[x] = self.doska[t1-x][t2]
				self.doska[t1-x][t2] = '*'
			else:
				a2[x] = 0
		for x in range(1, 8):
			if t2 - x < 8 and t2 - x >= 0 and self.doska[t1][t2-x] in y and ((x != 1 and a3[x-1] == 1) or (x == 1)):
				a3[x] = 1
				h3[x] = self.doska[t1][t2-x]
				self.doska[t1][t2-x] = '*'
			else:
				a3[x] = 0
		for x in range(1, 8):
			if t2 + x < 8 and t2 + x >= 0 and self.doska[t1][t2+x] in y and ((x != 1 and a4[x-1] == 1) or (x == 1)):
				a4[x] = 1
				h4[x] = self.doska[t1][t2+x]
				self.doska[t1][t2+x] = '*'
			else:
				a4[x] = 0
		self.vavod()
		for x in range(1, 8):
			if a1[x] == 1:
				self.doska[t1+x][t2] = h1[x]
		for x in range(1, 8):
			if a2[x] == 1:
				self.doska[t1-x][t2] = h2[x]
		for x in range(1, 8):
			if a3[x] == 1:
				self.doska[t1][t2-x] = h3[x]
		for x in range(1, 8):
			if a4[x] == 1:
				self.doska[t1][t2+x] = h4[x]
		
		
		
		
		if self.col == 'w' and self.name == 'R':
			y = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', 'p']
		elif self.col == 'b' and self.name == 'r':
			y = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P'] 	
		else:
			return False
		if (self.p1[0] == self.p2[0]) or (self.p1[1] == self.p2[1]):
			q = abs(int(self.p1[1]) - int(self.p2[1])) + abs(self.r.find(self.p1[0]) - self.r.find(self.p2[0]))
			if (self.r.find(self.p1[0]) == self.r.find(self.p2[0])):
				m2 = 0
			elif (self.r.find(self.p1[0]) < self.r.find(self.p2[0])):
				m2 = 1
			else:
				m2 = -1
			if int(self.p1[1]) == int(self.p2[1]):
				m1 = 0
			elif int(self.p1[1]) > int(self.p2[1]):
				m1 = -1
			else:
				m1 = 1
			e = ''
			z2 = self.r.find(self.p1[0])-2
			z1 = int(self.p1[1])
			for x in range(q):
				z1 += m1
				z2 += m2
				e += self.doska[8-z1][z2]
			if (e.count('.') == q) or ((e.count('.') == q-1 and e[-1] in y)):
				self.doska[8 - int(self.p2[-1])][self.r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
				self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2] = '.'
				return True
		return False

class Ferz(Doska):
	def __init__(self, name, col, p, doska, r='  ABCDEFGH  '):
		Doska.__init__(self, name, col, p, doska, r='  ABCDEFGH  ')
	def proverka(self):
		if self.col == 'w' and self.name == 'Q':
			y = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', 'p', '.']
		elif self.col == 'b' and self.name == 'q':
			y = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P', '.'] 	
		else:
			return False
		
		a1 = {}
		h1 = {}
		a2 = {}
		h2 = {}
		a3 = {}
		h3 = {}
		a4 = {}
		h4 = {}
			
		t1 = 8 - int(self.p1[1]) 
		t2 = self.r.find(self.p1[0])-2
		for x in range(1, 8):
			if t1 + x < 8 and t1 + x >= 0 and self.doska[t1+x][t2] in y and ((x != 1 and a1[x-1] == 1) or (x == 1)):
				a1[x] = 1
				h1[x] = self.doska[t1+x][t2]
				self.doska[t1+x][t2] = '*'
			else:
				a1[x] = 0
		for x in range(1, 8):
			if t1 - x < 8 and t1 - x >= 0 and self.doska[t1-x][t2] in y and ((x != 1 and a2[x-1] == 1) or (x == 1)):
				a2[x] = 1
				h2[x] = self.doska[t1-x][t2]
				self.doska[t1-x][t2] = '*'
			else:
				a2[x] = 0
		for x in range(1, 8):
			if t2 - x < 8 and t2 - x >= 0 and self.doska[t1][t2-x] in y and ((x != 1 and a3[x-1] == 1) or (x == 1)):
				a3[x] = 1
				h3[x] = self.doska[t1][t2-x]
				self.doska[t1][t2-x] = '*'
			else:
				a3[x] = 0
		for x in range(1, 8):
			if t2 + x < 8 and t2 + x >= 0 and self.doska[t1][t2+x] in y and ((x != 1 and a4[x-1] == 1) or (x == 1)):
				a4[x] = 1
				h4[x] = self.doska[t1][t2+x]
				self.doska[t1][t2+x] = '*'
			else:
				a4[x] = 0
		
		a11 = {}
		h11 = {}
		a12 = {}
		h12 = {}
		a13 = {}
		h13 = {}
		a14 = {}
		h14 = {}
			
		for x in range(1, 8):
			if t1 + x < 8 and t1 + x >= 0 and t2 + x < 8 and t2 + x >= 0 and self.doska[t1+x][t2+x] in y and ((x != 1 and a11[x-1] == 1) or (x == 1)):
				a11[x] = 1
				h11[x] = self.doska[t1+x][t2+x]
				self.doska[t1+x][t2+x] = '*'
			else:
				a11[x] = 0
		for x in range(1, 8):
			if t1 - x < 8 and t1 - x >= 0 and t2 + x < 8 and t2 + x >= 0 and self.doska[t1-x][t2+x] in y and ((x != 1 and a12[x-1] == 1) or (x == 1)):
				a12[x] = 1
				h12[x] = self.doska[t1-x][t2+x]
				self.doska[t1-x][t2+x] = '*'
			else:
				a12[x] = 0
		for x in range(1, 8):
			if t1 + x < 8 and t1 + x >= 0 and t2 - x < 8 and t2 - x >= 0 and self.doska[t1+x][t2-x] in y and ((x != 1 and a13[x-1] == 1) or (x == 1)):
				a13[x] = 1
				h13[x] = self.doska[t1+x][t2-x]
				self.doska[t1+x][t2-x] = '*'
			else:
				a13[x] = 0
		for x in range(1, 8):
			if t1 - x < 8 and t1 - x >= 0 and t2 - x < 8 and t2 - x >= 0 and self.doska[t1-x][t2-x] in y and ((x != 1 and a14[x-1] == 1) or (x == 1)):
				a14[x] = 1
				h14[x] = self.doska[t1-x][t2-x]
				self.doska[t1-x][t2-x] = '*'
			else:
				a14[x] = 0
		self.vavod()
		for x in range(1, 8):
			if a11[x] == 1:
				self.doska[t1+x][t2+x] = h11[x]
		for x in range(1, 8):
			if a12[x] == 1:
				self.doska[t1-x][t2+x] = h12[x]
		for x in range(1, 8):
			if a13[x] == 1:
				self.doska[t1+x][t2-x] = h13[x]
		for x in range(1, 8):
			if a14[x] == 1:
				self.doska[t1-x][t2-x] = h14[x]
		for x in range(1, 8):
			if a1[x] == 1:
				self.doska[t1+x][t2] = h1[x]
		for x in range(1, 8):
			if a2[x] == 1:
				self.doska[t1-x][t2] = h2[x]
		for x in range(1, 8):
			if a3[x] == 1:
				self.doska[t1][t2-x] = h3[x]
		for x in range(1, 8):
			if a4[x] == 1:
				self.doska[t1][t2+x] = h4[x]
		
		
		
		
		if self.col == 'w' and self.name == 'Q':
			y = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', 'p']
		elif self.col == 'b' and self.name == 'q':
			y = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P'] 	
		else:
			return False
		if (self.p1[0] == self.p2[0]) or (self.p1[1] == self.p2[1]) or (abs(self.r.find(self.p1[0]) - self.r.find(self.p2[0])) == abs(int(self.p1[1]) - int(self.p2[1]))):
			q = max(abs(int(self.p1[1]) - int(self.p2[1])), abs(self.r.find(self.p1[0]) - self.r.find(self.p2[0])))
			if (self.r.find(self.p1[0]) == self.r.find(self.p2[0])):
				m2 = 0
			elif (self.r.find(self.p1[0]) < self.r.find(self.p2[0])):
				m2 = 1
			else:
				m2 = -1
				
			if int(self.p1[1]) == int(self.p2[1]):
				m1 = 0
			elif int(self.p1[1]) > int(self.p2[1]):
				m1 = -1
			else:
				m1 = 1
			e = ''
			z2 = self.r.find(self.p1[0])-2
			z1 = int(self.p1[1])
			for x in range(q):
				z1 += m1
				z2 += m2
				e += self.doska[8-z1][z2]
			if (e.count('.') == q) or ((e.count('.') == q-1 and e[-1] in y)):
				self.doska[8 - int(self.p2[-1])][self.r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
				self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2] = '.'
				return True
		return False
		
		
class Korol(Doska):
	def __init__(self, name, col, p, doska, r='  ABCDEFGH  '):
		Doska.__init__(self, name, col, p, doska, r='  ABCDEFGH  ')
	def proverka(self):
		if self.col == 'w' and self.name == 'K':
			y = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', 'p', '.']
		elif self.col == 'b' and self.name == 'k':
			y = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P', '.'] 	
		else:
			return False
		
		a1 = {}
		h1 = {}
		a2 = {}
		h2 = {}
		a3 = {}
		h3 = {}
		a4 = {}
		h4 = {}
			
		t1 = 8 - int(self.p1[1]) 
		t2 = self.r.find(self.p1[0])-2
		for x in range(1, 2):
			if t1 + x < 8 and t1 + x >= 0 and self.doska[t1+x][t2] in y and ((x != 1 and a1[x-1] == 1) or (x == 1)):
				a1[x] = 1
				h1[x] = self.doska[t1+x][t2]
				self.doska[t1+x][t2] = '*'
			else:
				a1[x] = 0
		for x in range(1, 2):
			if t1 - x < 8 and t1 - x >= 0 and self.doska[t1-x][t2] in y and ((x != 1 and a2[x-1] == 1) or (x == 1)):
				a2[x] = 1
				h2[x] = self.doska[t1-x][t2]
				self.doska[t1-x][t2] = '*'
			else:
				a2[x] = 0
		for x in range(1, 2):
			if t2 - x < 8 and t2 - x >= 0 and self.doska[t1][t2-x] in y and ((x != 1 and a3[x-1] == 1) or (x == 1)):
				a3[x] = 1
				h3[x] = self.doska[t1][t2-x]
				self.doska[t1][t2-x] = '*'
			else:
				a3[x] = 0
		for x in range(1, 2):
			if t2 + x < 8 and t2 + x >= 0 and self.doska[t1][t2+x] in y and ((x != 1 and a4[x-1] == 1) or (x == 1)):
				a4[x] = 1
				h4[x] = self.doska[t1][t2+x]
				self.doska[t1][t2+x] = '*'
			else:
				a4[x] = 0
		
		a11 = {}
		h11 = {}
		a12 = {}
		h12 = {}
		a13 = {}
		h13 = {}
		a14 = {}
		h14 = {}
			
		for x in range(1, 2):
			if t1 + x < 8 and t1 + x >= 0 and t2 + x < 8 and t2 + x >= 0 and self.doska[t1+x][t2+x] in y and ((x != 1 and a11[x-1] == 1) or (x == 1)):
				a11[x] = 1
				h11[x] = self.doska[t1+x][t2+x]
				self.doska[t1+x][t2+x] = '*'
			else:
				a11[x] = 0
		for x in range(1, 2):
			if t1 - x < 8 and t1 - x >= 0 and t2 + x < 8 and t2 + x >= 0 and self.doska[t1-x][t2+x] in y and ((x != 1 and a12[x-1] == 1) or (x == 1)):
				a12[x] = 1
				h12[x] = self.doska[t1-x][t2+x]
				self.doska[t1-x][t2+x] = '*'
			else:
				a12[x] = 0
		for x in range(1, 2):
			if t1 + x < 8 and t1 + x >= 0 and t2 - x < 8 and t2 - x >= 0 and self.doska[t1+x][t2-x] in y and ((x != 1 and a13[x-1] == 1) or (x == 1)):
				a13[x] = 1
				h13[x] = self.doska[t1+x][t2-x]
				self.doska[t1+x][t2-x] = '*'
			else:
				a13[x] = 0
		for x in range(1, 2):
			if t1 - x < 8 and t1 - x >= 0 and t2 - x < 8 and t2 - x >= 0 and self.doska[t1-x][t2-x] in y and ((x != 1 and a14[x-1] == 1) or (x == 1)):
				a14[x] = 1
				h14[x] = self.doska[t1-x][t2-x]
				self.doska[t1-x][t2-x] = '*'
			else:
				a14[x] = 0
		self.vavod()
		for x in range(1, 2):
			if a11[x] == 1:
				self.doska[t1+x][t2+x] = h11[x]
		for x in range(1, 2):
			if a12[x] == 1:
				self.doska[t1-x][t2+x] = h12[x]
		for x in range(1, 2):
			if a13[x] == 1:
				self.doska[t1+x][t2-x] = h13[x]
		for x in range(1, 2):
			if a14[x] == 1:
				self.doska[t1-x][t2-x] = h14[x]
		for x in range(1, 2):
			if a1[x] == 1:
				self.doska[t1+x][t2] = h1[x]
		for x in range(1, 2):
			if a2[x] == 1:
				self.doska[t1-x][t2] = h2[x]
		for x in range(1, 2):
			if a3[x] == 1:
				self.doska[t1][t2-x] = h3[x]
		for x in range(1, 2):
			if a4[x] == 1:
				self.doska[t1][t2+x] = h4[x]
		
		
		if self.col == 'w' and self.name == 'K':
			y = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', 'p', '.']
		elif self.col == 'b' and self.name == 'k':
			y = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P', '.'] 	
		else:
			return False
		if self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] in y:
			if (int(self.p1[1]) + 1 == int(self.p2[1])) or (int(self.p1[1]) - 1 == int(self.p2[1])) or (int(self.p1[1]) == int(self.p2[1])):
				if (self.r.find(self.p1[0]) + 1 == self.r.find(self.p2[0])) or (self.r.find(self.p1[0]) - 1 == self.r.find(self.p2[0])) or (self.r.find(self.p1[0]) == self.r.find(self.p2[0])):
					self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
					self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2] = '.'
					return True
		return False
		
class Dvediagonali(Doska):
	def __init__(self, name, col, p, doska, r='  ABCDEFGH  '):
		Doska.__init__(self, name, col, p, doska, r='  ABCDEFGH  ')
	def proverka(self):
		if self.col == 'w' and self.name == 'D':
			y = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', 'p', '.', 'd']
		elif self.col == 'b' and self.name == 'd':
			y = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P', '.', 'D'] 	
		if (int(self.p1[1]) + 1 == int(self.p2[1]) or int(self.p1[1]) - 1 == int(self.p2[1])) and ((self.r.find(self.p1[0]) + 1 == self.r.find(self.p2[0])) or (self.r.find(self.p1[0]) - 1 == self.r.find(self.p2[0]))):
			if self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] in y:
				self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
				self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2] = '.'
				return True
		if (int(self.p1[1]) + 2 == int(self.p2[1]) and (self.r.find(self.p1[0]) == self.r.find(self.p2[0]))) or (int(self.p1[1]) - 2 == int(self.p2[1]) and (self.r.find(self.p1[0]) == self.r.find(self.p2[0]))):
			if self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] in y:
				self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
				self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2] = '.'
				return True
		return False
		
class Son(Doska):
	def __init__(self, name, col, p, doska, r='  ABCDEFGH  '):
		Doska.__init__(self, name, col, p, doska, r='  ABCDEFGH  ')
	def proverka(self):
		if self.col == 'w' and self.name == 'S':
			y = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', 'p', '.']
		elif self.col == 'b' and self.name == 's':
			y = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P', '.'] 	
		else:
			return False
		
		a1 = {}
		h1 = {}
		a2 = {}
		h2 = {}
		a3 = {}
		h3 = {}
		a4 = {}
		h4 = {}
			
		t1 = 8 - int(self.p1[1]) 
		t2 = self.r.find(self.p1[0])-2
		
		for x in range(1, 2):
			if t1 - x < 8 and t1 - x >= 0 and self.doska[t1-x][t2] in y and ((x != 1 and a2[x-1] == 1) or (x == 1)):
				a2[x] = 1
				h2[x] = self.doska[t1-x][t2]
				self.doska[t1-x][t2] = '*'
			else:
				a2[x] = 0
		for x in range(1, 2):
			if t2 - x < 8 and t2 - x >= 0 and self.doska[t1][t2-x] in y and ((x != 1 and a3[x-1] == 1) or (x == 1)):
				a3[x] = 1
				h3[x] = self.doska[t1][t2-x]
				self.doska[t1][t2-x] = '*'
			else:
				a3[x] = 0
		for x in range(1, 2):
			if t2 + x < 8 and t2 + x >= 0 and self.doska[t1][t2+x] in y and ((x != 1 and a4[x-1] == 1) or (x == 1)):
				a4[x] = 1
				h4[x] = self.doska[t1][t2+x]
				self.doska[t1][t2+x] = '*'
			else:
				a4[x] = 0
		
		a11 = {}
		h11 = {}
		a12 = {}
		h12 = {}
		a13 = {}
		h13 = {}
		a14 = {}
		h14 = {}
			
		
		for x in range(1, 2):
			if t1 - x < 8 and t1 - x >= 0 and t2 + x < 8 and t2 + x >= 0 and self.doska[t1-x][t2+x] in y and ((x != 1 and a12[x-1] == 1) or (x == 1)):
				a12[x] = 1
				h12[x] = self.doska[t1-x][t2+x]
				self.doska[t1-x][t2+x] = '*'
			else:
				a12[x] = 0
		
		for x in range(1, 2):
			if t1 - x < 8 and t1 - x >= 0 and t2 - x < 8 and t2 - x >= 0 and self.doska[t1-x][t2-x] in y and ((x != 1 and a14[x-1] == 1) or (x == 1)):
				a14[x] = 1
				h14[x] = self.doska[t1-x][t2-x]
				self.doska[t1-x][t2-x] = '*'
			else:
				a14[x] = 0
		self.vavod()
		for x in range(1, 2):
			if a12[x] == 1:
				self.doska[t1-x][t2+x] = h12[x]
		for x in range(1, 2):
			if a14[x] == 1:
				self.doska[t1-x][t2-x] = h14[x]
		
		for x in range(1, 2):
			if a2[x] == 1:
				self.doska[t1-x][t2] = h2[x]
		for x in range(1, 2):
			if a3[x] == 1:
				self.doska[t1][t2-x] = h3[x]
		for x in range(1, 2):
			if a4[x] == 1:
				self.doska[t1][t2+x] = h4[x]
		
		
		
		
		if self.col == 'w' and self.name == 'S':
			y = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', 'p', '.', 's']
		elif self.col == 'b' and self.name == 's':
			y = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P', '.', 'S'] 	
		else:
			return False
		if self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] in y:
			if (int(self.p1[1]) + 1 == int(self.p2[1])) or (int(self.p1[1]) == int(self.p2[1])):
				if (self.r.find(self.p1[0]) + 1 == self.r.find(self.p2[0])) or (self.r.find(self.p1[0]) == self.r.find(self.p2[0])):
					self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
					self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2] = '.'
					return True
		return False
		

class Odnadiagonali(Doska):
	
	
	def __init__(self, name, col, p, doska, r='  ABCDEFGH  '):
		Doska.__init__(self, name=name, col=col, p=p, doska=doska, r='  ABCDEFGH  ')
	def proverka(self):
		if self.col == 'w' and self.name == 'O':
			y = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', 'p', '.']
		elif self.col == 'b' and self.name == 'o':
			y = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P', '.'] 	
		else:
			return False
		
		
		a1 = {}
		h1 = {}
		a2 = {}
		h2 = {}
		a3 = {}
		h3 = {}
		a4 = {}
		h4 = {}
			
		
		t1 = 8 - int(self.p1[1]) 
		t2 = self.r.find(self.p1[0])-2
		for x in range(1, 2):
			if t1 + x < 8 and t1 + x >= 0 and t2 + x < 8 and t2 + x >= 0 and self.doska[t1+x][t2+x] in y and ((x != 1 and a1[x-1] == 1) or (x == 1)):
				a1[x] = 1
				h1[x] = self.doska[t1+x][t2+x]
				self.doska[t1+x][t2+x] = '*'
			else:
				a1[x] = 0
		for x in range(1, 2):
			if t1 - x < 8 and t1 - x >= 0 and t2 + x < 8 and t2 + x >= 0 and self.doska[t1-x][t2+x] in y and ((x != 1 and a2[x-1] == 1) or (x == 1)):
				a2[x] = 1
				h2[x] = self.doska[t1-x][t2+x]
				self.doska[t1-x][t2+x] = '*'
			else:
				a2[x] = 0
		for x in range(1, 2):
			if t1 + x < 8 and t1 + x >= 0 and t2 - x < 8 and t2 - x >= 0 and self.doska[t1+x][t2-x] in y and ((x != 1 and a3[x-1] == 1) or (x == 1)):
				a3[x] = 1
				h3[x] = self.doska[t1+x][t2-x]
				self.doska[t1+x][t2-x] = '*'
			else:
				a3[x] = 0
		for x in range(1, 2):
			if t1 - x < 8 and t1 - x >= 0 and t2 - x < 8 and t2 - x >= 0 and self.doska[t1-x][t2-x] in y and ((x != 1 and a4[x-1] == 1) or (x == 1)):
				a4[x] = 1
				h4[x] = self.doska[t1-x][t2-x]
				self.doska[t1-x][t2-x] = '*'
			else:
				a4[x] = 0
		self.vavod()
		for x in range(1, 2):
			if a1[x] == 1:
				self.doska[t1+x][t2+x] = h1[x]
		for x in range(1, 2):
			if a2[x] == 1:
				self.doska[t1-x][t2+x] = h2[x]
		for x in range(1, 2):
			if a3[x] == 1:
				self.doska[t1+x][t2-x] = h3[x]
		for x in range(1, 2):
			if a4[x] == 1:
				self.doska[t1-x][t2-x] = h4[x]
		
		
		
		if self.col == 'w' and self.name == 'O':
			y = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', 'p', '.', 'o']
		elif self.col == 'b' and self.name == 'o':
			y = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', 'P', '.', 'O'] 	
		if (int(self.p1[1]) + 1 == int(self.p2[1]) or int(self.p1[1]) - 1 == int(self.p2[1])) and ((self.r.find(self.p1[0]) + 1 == self.r.find(self.p2[0])) or (self.r.find(self.p1[0]) - 1 == self.r.find(self.p2[0]))):
			if self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] in y:
				self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
				self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2] = '.'
				return True
		return False

class Сhecke(Doska):
	def __init__(self, name, col, p, doska, r='  ABCDEFGH  '):
		Doska.__init__(self, name=name, col=col, p=p, doska=doska, r='  ABCDEFGH  ')
	def proverka(self):
		if self.col == 'w' and self.name == 'A':
			y = 'a'
		elif self.col == 'b' and self.name == 'a':
			y = 'A'	
		if col == 'b':
			if self.p3 == ''  and ((self.col == 'w' and self.name == 'A') or (self.col == 'b' and self.name == 'a')):
				if ((int(self.p1[1]) + 1 == int(self.p2[1]) or int(self.p1[1]) - 1 == int(self.p2[1])) and ((self.r.find(self.p1[0]) + 1 == self.r.find(self.p2[0])))) :
					if self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] == '.':
						self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
						self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2] = '.'
						return True
				elif ((int(self.p1[1]) + 2 == int(self.p2[1]) or int(self.p1[1]) - 2 == int(self.p2[1])) and ((self.r.find(self.p1[0]) + 2 == self.r.find(self.p2[0])))):
					if self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] == '.':
						if (int(self.p1[1]) + 2 == int(self.p2[1]) or int(self.p1[1]) - 2 == int(self.p2[1])) and ((self.r.find(self.p1[0]) + 2 == self.r.find(self.p2[0]))):
							self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
							self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2] = '.'
							self.doska[8 - int(self.p1[1])-1][self.r.find(self.p1[0])-1] = '.'
							return True
								
			else:
				while self.p2 != '':
					if self.doska[8 - int(self.p1[1]+1)][self.r.find(self.p1[0])-2+1] == y or self.doska[8 - int(self.p1[1])-1][self.r.find(self.p1[0])-2+1] == y:
						if self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] == '.':
							if (int(self.p1[1]) + 2 == int(self.p2[1]) or int(self.p1[1]) - 2 == int(self.p2[1])) and ((self.r.find(self.p1[0]) + 2 == self.r.find(self.p2[0]))):
								self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
								self.doska[8 - int(self.p1[1])+1][self.r.find(self.p1[0])+1] = 'E'
								self.doska[8 - int(self.p1[1])+2][self.r.find(self.p1[0])+2] = 'Q'
								p1 = p2
								p2 = p3[:3]
								return True
		if col == 'w':
			if self.p3 == ''  and ((self.col == 'w' and self.name == 'A') or (self.col == 'b' and self.name == 'a')):

				if ((int(self.p1[1]) + 1 == int(self.p2[1]) or int(self.p1[1]) - 1 == int(self.p2[1])) and ((self.r.find(self.p1[0]) - 1 == self.r.find(self.p2[0])))) :
					if self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] == '.':
						self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
						self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2] = '.'
						return True
				elif ((int(self.p1[1]) + 2 == int(self.p2[1]) or int(self.p1[1]) - 2 == int(self.p2[1])) and ((self.r.find(self.p1[0]) - 2 == self.r.find(self.p2[0])))):
					if self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] == '.':
						if (int(self.p1[1]) + 2 == int(self.p2[1]) or int(self.p1[1]) - 2 == int(self.p2[1])) and ((self.r.find(self.p1[0]) + 2 == self.r.find(self.p2[0]))):
							self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
							self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2] = '.'
							self.doska[8 - int(self.p1[1])-1][self.r.find(self.p1[0])-1] = '.'
							return True
							
			
			else:
				while self.p2 != '':
					if self.doska[8 - int(self.p1[1]+1)][self.r.find(self.p1[0])-2+1] == y or self.doska[8 - int(self.p1[1]-1)][self.r.find(self.p1[0])-2+1] == y:
						if self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] == '.':
							if (int(self.p1[1]) + 2 == int(self.p2[1]) or int(self.p1[1]) - 2 == int(self.p2[1])) and ((self.r.find(self.p1[0]) - 2 == self.r.find(self.p2[0]))):
								self.doska[8 - int(self.p2[-1])][r.find(self.p2[-2])-2] = self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2]
								self.doska[8 - int(self.p1[1])][self.r.find(self.p1[0])-2] = '.'
								p1 = p2
								p2 = p3[:3]
								return True
		print(0)
		return False

#основная доска


dosk = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], ['p']*8, ['.'] * 8, ['.'] * 8, ['.'] * 8, ['.'] * 8, ['P']*8, ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
name=''
p=''
col = 'b'
d = Doska(name, col, p, dosk)
d.vavod()
hn=''
r = '  ABCDEFGH  '
i = 1
q = True
while q:
	fl = False
	while not fl and q:
		print('ход №:', i)
		col = d.cooll(i)
		p = input() # ход
		if p == 'НАЗАД':
			i -= 2					
		if q == 'STOP':
			q = False
			break
		d = Doska(name, col, p, dosk)	
		#возвращение хода	
		if p != 'НАЗАД':
			p1 = p[:2]
			p2 = p[-2:]
			hn += p[:2] + dosk[8 - int(p1[1])][r.find(p1[0])-2] + p2 + dosk[8 - int(p2[1])][r.find(p2[0])-2]

		fl = d.hod(hn)
		if fl:
			dosk = d.doska
			fl = True
		else:
			hn = hn[:-6]
			print('False')
		d.vavod()
		print()
		if not (d.provkor):
			q = False
	i += 1
	w = p
print('ИГРА ЗАВЕРШЕНА')



# 1 доп

# 1 фигура - две диагонали. ход либо по диагонали на 1 шаг, либо на 2 клетки вперед/назад
'''

dos = [['.']*8, ['.']*8, ['p'] * 8, ['p'] * 8, ['D'] * 8, ['.'] * 8, ['.']*8, ['.'] * 8]

#выводим доску	
print('-----------------------')
print('|   A B C D E F G H   |')
print('|                     |')
i = 8
for x in dos:
	print('|', i, *x, i, '|')
	i -=1
print('|                     |')
print('|   A B C D E F G H   |')
print('-----------------------')
col = 'w'
while True:
	p = input()
	r = '  ABCDEFGH  '
	f = Dvediagonali(dos[8 - int(p[1])][r.find(p[0])-2], col, p, dos)

	if p == 'STOP':
		break
	col = 'w'
	t = f.proverka()
	if t:
		dos = f.doska
		fl = True
	else:
		print('False')
	
	#выводим доску	
	print('-----------------------')
	print('|   A B C D E F G H   |')
	print('|                     |')
	i = 8
	for x in dos:
		print('|', i, *x, i, '|')
		i -=1
	print('|                     |')
	print('|   A B C D E F G H   |')
	print('-----------------------')
	print()
'''
# 2 фигура - сын. ход на 1 клетку влево, вправо, вверх, по диагонали
'''dos = [['.']*8, ['.']*8, ['p'] * 8, ['p'] * 8, ['S'] * 8, ['.'] * 8, ['.']*8, ['.'] * 8]

#выводим доску	
print('-----------------------')
print('|   A B C D E F G H   |')
print('|                     |')
i = 8
for x in dos:
	print('|', i, *x, i, '|')
	i -=1
print('|                     |')
print('|   A B C D E F G H   |')
print('-----------------------')
col = 'w'
while True:
	p = input()
	r = '  ABCDEFGH  '
	f = Son(dos[8 - int(p[1])][r.find(p[0])-2], col, p, dos)

	if p == 'STOP':
		break
	col = 'w'
	t = f.proverka()
	if t:
		dos = f.doska
		fl = True
	else:
		print('False')
	
	#выводим доску	
	print('-----------------------')
	print('|   A B C D E F G H   |')
	print('|                     |')
	i = 8
	for x in dos:
		print('|', i, *x, i, '|')
		i -=1
	print('|                     |')
	print('|   A B C D E F G H   |')
	print('-----------------------')
	print()
'''

# 3 фигура - одна диагональ. ход на 1 клетку по диагонали
'''
dos = [['.']*8, ['.']*8, ['p'] * 8, ['p'] * 8, ['O'] * 8, ['.'] * 8, ['.']*8, ['.'] * 8]

#выводим доску	
print('-----------------------')
print('|   A B C D E F G H   |')
print('|                     |')
i = 8
for x in dos:
	print('|', i, *x, i, '|')
	i -=1
print('|                     |')
print('|   A B C D E F G H   |')
print('-----------------------')
col = 'w'
while True:
	p = input()
	r = '  ABCDEFGH  '
	f = Odnadiagonali(dos[8 - int(p[1])][r.find(p[0])-2], col, p, dos)

	if p == 'STOP':
		break
	col = 'w'
	t = f.proverka()
	if t:
		dos = f.doska
		fl = True
	else:
		print('False')
	
	#выводим доску	
	print('-----------------------')
	print('|   A B C D E F G H   |')
	print('|                     |')
	i = 8
	for x in dos:
		print('|', i, *x, i, '|')
		i -=1
	print('|                     |')
	print('|   A B C D E F G H   |')
	print('-----------------------')
	print()
'''
'''
#3 шашки
#A W
dosk = [['.', 'A', '.', 'A', '.', 'A', '.', 'A'], ['A', '.', 'A', '.', 'A', '.', 'A', '.'],['.', 'A', '.', 'A', '.', 'A', '.', 'A'], ['.'] * 8, ['.'] * 8, ['a', '.', 'a', '.', 'a', '.', 'a', '.'], ['.', 'a', '.', 'a', '.', 'a', '.', 'a'], ['a', '.', 'a', '.', 'a', '.', 'a', '.']]
name=''
p=''
col = 'w'
d = Doska(name, col, p, dosk)
d.vavod()
hn=''
r = '  ABCDEFGH  '
i = 1
q = True
while q:
	fl = False
	while not fl and q:
		print('ход №:', i)
		col = d.cooll(i)
		p = input() # ход
		if p == 'НАЗАД':
			i -= 2					
		if q == 'STOP':
			print(6)
			q = False
			break
		d = Doska(name, col, p, dosk)	
		fl = d.hod(hn)
		if fl:
			dosk = d.doska
			fl = True
		else:
			print('7')
			print('False')
		d.vavod()
		print()
		if not (d.provkor):
			print('55555555555')
			q = False
	i += 1
	w = p
	print(hn)
print('ИГРА ЗАВЕРШЕНА')
'''
