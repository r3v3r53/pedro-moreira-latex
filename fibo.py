# -*- coding: utf-8 -*-
'''
autor: Jose Jasnau Caeiro
data: 12 de marco de 2012
obs.: realizacoes das funcoes de calculo
      dos numeros de fibonacci
'''

def fibonacci_recursivo(n):
	'''
	realizacao recursiva do calculo dos numeros de
	fibonacci
	n - argumento inteiro positivo
	'''
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci_recursivo(n-2) +\
				fibonacci_recursivo(n-1)

def fibonacci_iterativo(n):
	'''
	realizacao iterativa
	'''
	i = 1
	j = 0
	for k in range(n):
		t = i + j
		i, j = j, t
		pass
	return j	
	
		
