# -*- coding: utf-8 -*-

from fibo import fibonacci_iterativo

import time


for n in range(150000,250000, 5000):
	t1 = time.clock()
	fibonacci_iterativo(n)
	t2 = time.clock()
	print n, t2-t1
	pass
