"""
Siguiendo lo que hice una vez con polinomios, reharé lo que hice aquella vez pero está vez usare tuplas en lugar de listas. Mi experiencia con Gram-Schmit me mostro que usar listas podría darme algunos problemas.

"""
class Polinomio:
	def __init__ (self, coe=[0]):
		# una lista con los coeficientes donde el numero en la posición self.ce[i] corresponde al coeficiente del termino x^i
		self.ce=tuple(coe)
	
	# Lo siguiente es el sobrecargo de los operadores "+", "*", "-" y "=="
	def __add__(self,pol):
		if len(pol.ce) < len(self.ce):
			aux = []
			for k in range(0,len(pol.ce)):
				aux.append(pol.ce[k] + self.ce[k])
			for k in range(len(pol.ce),len(self.ce)):
				aux.append(self.ce[k])
			return Polinomio(aux)
		else:
			aux = []
			for k in range(0,len(self.ce)):
				aux.append(pol.ce[k] + self.ce[k])
			for k in range(len(self.ce),len(pol.ce)):
				aux.append(pol.ce[k])
			return Polinomio(aux)
			
	def __mul__(self, pol):
		if type(pol) == Polinomio:
			grad = self.grado()+pol.grado() + 1
			pro = []
			if self.grado()>pol.grado():
				for k in range(0,grad):
					aux = 0
					for j in range(k-len(self.ce),len(self.ce)):
						if j>=0 and k-j>=0 and k-j < len(pol.ce):
							aux = aux + self.ce[j]*pol.ce[k-j]
					pro.append(aux)
			else:
				for k in range(0,grad):
					aux = 0
					for j in range(k-len(pol.ce),len(pol.ce)):
						if j>=0 and k-j>=0 and k-j < len(self.ce):
							aux = aux + pol.ce[j]*self.ce[k-j]
					pro.append(aux)
			return Polinomio(pro)
		else:
			pro = []
			for coe in self.ce:
				pro.append(coe * pol)
			return Polinomio(pro)
	
	def __sub__(self,pol):
		if len(pol.ce) < len(self.ce):
			aux = []
			for k in range(0,len(pol.ce)):
				aux.append( self.ce[k]-pol.ce[k])
			for k in range(len(pol.ce),len(self.ce)):
				aux.append(self.ce[k])
			return Polinomio(aux)
		else:
			aux = []
			for k in range(0,len(self.ce)):
				aux.append(self.ce[k]-pol.ce[k])
			for k in range(len(self.ce),len(pol.ce)):
				aux.append(-pol.ce[k])
			return Polinomio(aux)
			
	def __eq__(self,pol):
		if self.ce == pol.ce:
			return True
		else:
			return False
	
	# regresa el polinomio en una lista con el mejor formato que pude darle hasta la fecha Jul/2022
	def formato(self):
		aux=[]
		for k in range(0,len(self.ce)):
			if k==0: 
				aux.append(f"{self.ce[k]} +")
			if k and k< len(self.ce)-1 and self.ce[k]!=0:
				aux.append(f"{self.ce[k]}x^{k} +")
			if  k==len(self.ce)-1 and self.ce[k]!=0 and k:
				aux.append(f"{self.ce[k]}x^{k}")
		return aux
	#Imprime el polinomio con el formato de arriba
	def impri(self):
		print(*self.formato())

	#Regresa el grado del polinomio.
	def grado(self):
		return len(self.ce)-1
		
#Dado un polinomio y un punto, se evalua el polinomio en el punto dado.

def evapol(pol,x0=0):
	val = 0
	n = len(pol.ce)
	for i in range (0,n):
		val = pol.ce[n - i-1] + val * x0
	return val

#Se calcula la integral de un polinomio en un intervalo [a,b]. Se hace con la fórmula cerrada de integración.

def intpol(pol,a,b):
	aux = 0
	for k in range(0,len(pol.ce)):
		aux = aux + pol.ce[k]*b**(k+1)/(k+1) - pol.ce[k]*a**(k+1)/(k+1)
	return aux
