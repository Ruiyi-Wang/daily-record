import os
def test():
	c = range(10)
	print (type(c))
	print ([x for x in c])
	print ([d for d in os.listdir('.')])
	d = {'x':'A','y':'B','z':'C'}
	L = ['hello','world','IBM','Apple']
	d1 = [s.lower() for s in L]
	print (L.d1)
	d2 = [k + '=' + v for k, v in d.items()]

def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a,b=b,a+b
		n=n+1
def test():
	for i in fib(100):
		print(i)

def f(x):
	return x*x+1
def test():
	r = map(f, [1,2,3,4,5,6,7,8,9])
	print (r)
	for i in r:
		print (i)

def test():
	s = '123'
	print (int(s)+10)
	print (s+str(10))
	print (int(s)+int(10))
	print (str(s)+str(10))

def main():
	test()
if __name__ == '__main__':
	main()
