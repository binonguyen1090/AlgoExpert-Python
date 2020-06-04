def getNthFib(n, memorize={1: 0, 2: 1}):
	if n in memorize:
		return memorize[n]
	else:
		memorize[n] = getNthFib(n-1, memorize) + getNthFib(n-2, memorize)
		return memorize[n]
