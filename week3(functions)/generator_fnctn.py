range(10)
for i in range(10):
    print(i)

def test_fib(n):
    a,b=0,1
    for i in range(n):
        yield a
        a,b=b,a+b
for i in test_fib(10):
    print(i)

def test_fib1():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
fib= test_fib1()
for i in range(10):
    print(next(fib))

s='jain'
for i in s:
    print(i)
s1=iter(s)
print(next(s1))
print(next(s1))
print(next(s1))
print(next(s1),end='\n\n')