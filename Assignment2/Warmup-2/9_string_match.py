def string_match(a, b):
	a_sub = [a[i:i+2] for i in range(len(a)-1)]
	b_sub = [b[i:i+2] for i in range(len(b)-1)]
	return list(map(lambda x, y: x == y, a_sub, b_sub)).count(True)
