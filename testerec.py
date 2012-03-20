# -*- coding: utf-8 -*-

from fibo import fibonacci_recursivo

import time

N = 36

for n in range(N):
	t1 = time.clock()
	fibonacci_recursivo(n)
	t2 = time.clock()
	print n, t2-t1
	pass


