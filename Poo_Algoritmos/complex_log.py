import math
import time 

class Complejidad_algoritmica:
	def __init__(self, n):
		self.n = n

	def constante(self):
		return 1

	def logaritmica(self):
		return math.log10(self.n)

	def lineal(self):
		return self.n

	def log_lineal(self):	
		return self.n * math.log10(self.n)

	def	polinomial(self):
		return self.n**2

	def	exponencial(self):
		return 2**self.n


def main():
	
    nums = [1, 10, 100, 1000, 10000]
    
    for n in nums:
        
        complejidad = Complejidad_algoritmica(n)
        
        print('n es igual a: {}'.format(n))
        
        principio = time.time()
        print(f'El resultado de complejidad constante para n igual a {n} es: ', complejidad.constante())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        principio = time.time()
        print(f'El resultado de complejidad logaritmica para n igual a {n} es: ', complejidad.logaritmica())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        principio = time.time()
        print(f'El resultado de complejidad lineal para n igual a {n} es: ', complejidad.lineal())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        principio = time.time()
        print(f'El resultado de complejidad logaritmica lineal para n igual a {n} es: ', complejidad.log_lineal())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        principio = time.time()
        print(f'El resultado de complejidad polinomial para n igual a {n} es: ', complejidad.polinomial())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
       
        principio = time.time()
        print(f'El resultado de complejidad exponencial para n igual a {n} es: ', complejidad.exponencial())
        fin = time.time()
        tiempo = fin - principio
        print(f'has tardado {tiempo} segundos\n')
        
        print('\n\n')

if __name__ == '__main__':
    
    main()