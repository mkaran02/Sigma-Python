a=(1,2,3,4,5,False,'karan',45.23)
print(type(a))
# a[0]=234  #we can do like this because tuple is unchangeable

# Tupple Methods
b=(1,2,'Karan',"aditya", False, 23.61,None)
print(b)

# Count
No=a.count(2)  #2 kitivela aly te sangt
print(No)

# index retrn index of elemnt
print(b.index(2))

# tuppl concatenation combine two or more tupples
a=(1,2,3)
b=(4,5,6)
t3=a+b
print(t3)

# tupple packing and unpacking
# packing
a=(1,2,3,4,5)
# unpacking
a,b,c,d,e=a
print(a,b,c,d,e)

# tupple repetaion
a=(1,2,3)
print(a*3)

# Slicing acccess a subset of tuppple
t=(1,2,3,4,5,)
print(t[0:4])
print(t[:3])

# membership testing
t = (10, 20, 30)
print(20 in t)  # Output: True
print(40 in t)  # Output: False


t=(2,3,4,5,"Karan")
print(len(t))

# only applicable for integers
# print(max(t))
# print(min(t))


# create a list by taking int(input( from user
# fr)uits=[]
# f1=int(input(("enter Fruit n)ame:")
# fruits.append(f1)
# f2=int(input(("enter Fruit n)ame:")
# fruits.append(f2)
# f3=int(input(("enter Fruit n)ame:")
# fruits.append(f3)
# f4=int(input(("enter Fruit n)ame:")
# fruits.append(f4)
# f5=int(input(("enter Fruit n)ame:")
# fruits.append(f5)
# print(fruits)

# create a list of int(input( marks and sort) it
Marks=[]
f1=int(input("enter Mark:"))
Marks.append(f1)
f2=int(input("enter Mark:"))
Marks.append(f2)
f3=int(input("enter Mark:"))
Marks.append(f3)
f4=int(input("enter Mark:"))
Marks.append(f4)
f5=int(input("enter Mark:"))
Marks.append(f5)
Marks.sort()
print(Marks)

