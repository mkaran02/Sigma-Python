set={1,2,3,4, 'Karan'}
print(set)
# e=set() #empty set

#set mthods
set.add(43636)
print(set)

set.update([22,323,124])
print(set)

set.remove(2)
print(set)

set.discard(23)
print(set)

set.clear()
print(set)

#operations
# union
s1={1,2,3,4}
s2={5,6,7}
print(s1.union(s2))
print(s1 | s2)

#intersection
print(s1.intersection(s2))
print(s1 & s2)

print(s1.difference(s2))
print(s1-s2)

print(s1.symmetric_difference(s2))
print(s1^s2)

#chec if the set is subest or not and rturn true or false
print(s1.issubset(s2))
print(s1.issuperset(s2))
print(s1.isdisjoint(s2))



