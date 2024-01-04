#lists are mutable

l=[2,'kritika',45.34 , 'hyyy', True]
l1=[3,0,5]
l2=[4,1,8,90,12,34,2]
l3=['anisha' , 'kritika' , 'khushi']
l4=[7,3,1]
s="jiya"

#some basic operations on list
print(l)
print(l[::2])
print(list(s))
print(list(s)+l)
print(l[3])
print(l[3][0:2])
print(l+l1) 
print(l1*3)
print(len(l))

# to add something in the list in a unit
l.append(5)
print(l)
l.append(s)
print(l)
l.append(l1)
print(l)
print(l[-1][1])

# insert data in last of list but in scattered manner
l.extend('kri')
print(l)
l.extend(l1)
print(l)
l.extend([1,34,55])
print(l)

# insert data at a particular place
l1.insert(1,'kritika')
print(l1)
l1.insert(3,[5,7,1])
print(l1)
l1.insert(-1 , 45)
print(l1)

#to delete from last and acc to index
l1.pop()
print(l1)
l1.pop(2)
print(l1)

#remove first occurence of (value)
l1.remove(3)
print(l1)
l1[1].remove(7)
print(l1)

#to reverse
print(l1[::-1])
l1.reverse()
print(l1)

#sort
l2.sort()
print(l2)
l3.sort()
print(l3)
l3.sort(reverse=True)
print(l3)

print(l3.index("kritika"))
print(l3.count("kritika"))
l4[0]=56
print(l4)

#replace letter of string temporary
print(s.replace('j' , 'p'))
print(s)