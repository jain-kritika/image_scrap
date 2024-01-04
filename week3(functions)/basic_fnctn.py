# def test():
#     print("this is my first function")
# print(test())

#we use return in functions
def test1():
    return "this is my first return"
print(test1())
print(test1()+' kritika')

def test2():
    return 'jiya' , 56.5 , [4,5]
print(test2())

a,b,c=test2()
print(a)
print(b)
print(c)

def test3():
    d=5+6/7
    return d
print(test3())

def test4(e,f,g):
    h=e+f/g
    return h
print(test4(2,5,8))

def test5(l,m):
    return l+m
print(test5(4,5))
print(test5('kritika' , ' jain'))
print(test5([2,3,5] , [6,7,0]))

l=[1,3,2,'jiya',67.2,'kritika' , 56 , [1,2,3,4]]
def test6(l):
    l1=[]
    for i in l:
        if type(i)==int or type(i)==float:
            l1.append(i)
    return l1
print(test6(l) , end='\n\n')

def test7(b):
    l=[]
    for i in b:
        if type(i)==list:
            for j in i:
              l.append(j)
        else:
            if type(i)==int or type(i)==float:
                l.append(i)
    return l
print(test7(l), end='\n\n')

# *means you can pass n no of args inside a fnctn
def test8(*args):
    return args
print(test8(1,2,3))
print(test8(1,3,'kr' , 'it' , 'ika' , 78.2))

def test9(*args , a):
    return args , a
print(test9(1,2,3 , a=23))

def test10(a,b,c=45,d=12):
    return a,c,b,d
print(test10(1,40))
print(test10(1,40 , c=0))

def test11(**kwargs):
    return kwargs
print(test11(a=45 , b='jain' , c=45.5 , d=[78,12,15.46]))