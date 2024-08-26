a = frozenset([1,2,3,4,5])
c = frozenset([3,4,7,8])
print(a)
for i in a:
    print(i)
print(40 in a)
#copy()
b = a.copy()
print(b)
#union()
print("union : ",a.union(c))  
#intersection
print("intersection : ",a.intersection(c))  
#set difference 
print("set difference : ",a.difference(c))   
#symmetric difference 
print("symmetric_difference : ",a.symmetric_difference(c))
mset = set(a)
print(mset)