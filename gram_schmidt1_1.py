import numpy as np
import matplotlib.pyplot as plt

#En este módulo se usa para toda el álgebra de los polinomios así cómo sus integrales.

import Polinomios1_1 as pol

# Estas dos funciones son tal cual la función dada. La función que se aproximará y abajo la que se usa para graficar
def f(x):
	if x<=-.33:
		return abs(x)
	elif  x<=.33:
		return 1
	else:
		return abs(2*x)
	 
def f1(x):
	y=[]
	for num in x:
		y.append(f(num))
	return y

#Aquí calculo las integrales necesarias con el método del trapecio. Tengo entendido que hay formas de integrar con python pero quise usar lo visto en clase.
# Esta función sólo calcula las integrales de la funciones p(x)f(x), donde f(x) es 
# la función de arriba y p(x) es un polinomio. Las integrales de polinomio se hacen
# en el módulo Polinomios.

def integral(f,a,b, p = pol.Polinomio([1])):
	ite = 100000
	h = (b-a)/ite
	inte = 0
	for i in range(ite+1):
		inte +=f(a + h*i)*pol.evapol(p,a + h*i)
	for i in range(1,ite):
		inte +=f(a + h*i)*pol.evapol(p,a + h*i)
	return h*inte*.5

#Dado una base ortonormal, aquí se hace la proyección. 
#Es el mismo proceso que en \R^n

def Proyeccion(f,a,b,GM):
	Aprox = pol.Polinomio([0])
	for poli in GM:
		c = integral(f,a,b,poli)
		Aprox = Aprox + (poli * c)
	return Aprox
		
#Se genera la base de ortornomal a partir de la base ${1,x,x^2,\ldots,x^n}$.
#Es el mismo proceso que en \R^n
		
def gramshmidt(Base,a,b):
	Base[0] = Base[0]*(1/((b-a)**.5))
	GM = [Base[0]]
	for i in range(1,len(Base)):
		aux = 0
		gm = pol.Polinomio([0])
		for poli in GM:
			c = pol.intpol(Base[i]*poli,a,b)
			gmaux = poli*c
			gm = gm + gmaux
		gm = Base[i] - gm
		c = pol.intpol(gm*gm,a,b)**.5
		gm = gm * (1/c)
		GM.append(gm)
	return GM

print("Grado máximo del polinomio para aproximar.")
n = int(input())
BA = []
for i in range(n+1):
	a = []
	for j in range(i+1):
		if j==i:
			a.append(1)
		else:
			a.append(0)
	aux = pol.Polinomio(a)
	BA.append(aux)

GM = gramshmidt(BA,-1,1)

#El siguiente bloque escribia los polinomios en un archivo de texto para evitar calcularlos de nuevo.

#with open("1.txt",'w') as docu:
#		for pol in GM:
#			a = " ".join([f"{num} " for  num in pol.ce])
#			docu.write(f"{a}\n")



#Se obitene la aproximación	
Aprox = Proyeccion(f,-1,1,GM)

x = np.arange(-1,1+.01,0.01)
fx = f1(x)

#Se grafica la función deseada y el polinomio que lo apróxima.

plt.figure()
plt.plot(x, fx, 'k', x, pol.evapol(Aprox,x), 'r') 

plt.show()
