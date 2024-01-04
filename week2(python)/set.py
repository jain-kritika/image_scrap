s={}
print(type(s))
s1={2,4,1,3}
print(type(s1) , end='\n')

#set list accept ni krta tuple ko kr leta h i.e. immutable collection rlhta h
s2={2,56,34,(2,4) , "kritika"}
print(s2 , end='\n')

s3={1,4,1,6,7,6,2,4,7,0,0,3,34,34,12,4,3 , 'jiya' , 'Jiya'}
print(s3, end='\n')

l1=[4,2,3,1,2]
print(set(l1))

s1.add(5)
print(s1)
s1.remove(2)
print(s1)
