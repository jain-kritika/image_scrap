d={}
print(type(d))
#d={key:value} key should be unique otherwise it will overwrite next value
d1={'key' : 'kritika'}
print(type(d1), end='\n')
d2={'name' : 'kritika' , 'course' : 'BTech'}
print(type(d2), end='\n')
d3={234:'jiya' , True:568}
print(type(d3), end='\n')
print(d3[234], end='\n')

#as true=1 and false =0
print(d3[True], end='\n')
print(d3[1], end='\n\n')

d4={'name' : 'kritika' , 'course' : ['BTech' , 'python']}
print(d4['course'], end='\n')
print(d4['course'][1], end='\n\n')

d5={'number':[34,12,45] , 'assignment':(3,5,2) , 'date':{12,31} , 'classtime' : {'python':5 , 'java':9}}
print(d5, end='\n')
print(d5['classtime']['python'], end='\n\n')

#to add a key
d5['mentor']=['jiya','janu','ganeshu','choti']

#to delete
del d5['number']
print(d5, end='\n\n')

#to show all keys or values
print(d5.keys(), end='\n')
print(d5.values(), end='\n\n')
#to show in list
print(list(d5.keys()), end='\n\n')
print(list(d5.values()), end='\n\n')
print(list(d5.items()), end='\n\n')

#to delete
d5.pop('assignment')
print(d5 , end='\n\n')

#if else
# marks=10 or
marks=int(input("enter the marks:"))
if marks>=80:
    print("you will be a part of a0 batch")
elif marks>=60 and marks<80:
    print("you will be a part of a1 batch")
elif marks<60 and marks>40:
    print("you will be a part of a2 batch")
else:
    print("you will be a part of a3 batch")

#input is always string but we can chnage its datatype by applying int , float , etc.
marks=input("enter marks::")
print(type(marks))
marks=int(input("enter marks::"))
print(type(marks))

#loop
l=[1,2,3,4,5,6,7,8]
l1=[]
for i in l:
    print(i+1)
    l1.append(i+1)
    print(l1)
    print(l)

l2=['kriti' , 'vats']
l3=[]
for i in l2:
    print(i)
    l3.append(i.upper())
    print(l3 , end='\n\n')

l4=[4,56.7,'kritika' , 'ft' , 78]
l5_num=[]
l6_str=[]
for i in l4:
    if type(i)==int or type(i)==float:
        l5_num.append(i)
    else:
        l6_str.append(i)
        print(l5_num)
        print(l6_str)