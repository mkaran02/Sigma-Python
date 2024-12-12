# mylist=["apple" ,"orange",'cherry', 5, 45.9,True,"Akash" ]
# print(mylist)
# print(mylist[0])
# mylist[0]="banana"
# print(mylist[0])
# # lists are mutable means changable and cn be accessed using index which starts from 0. List is of differnent sata types
# print(mylist[0:4])

# # we can also use list() to create list
# a=list(("Karan",'kaaa',2,23.23))
# print(a)

# list methods
mylist=["apple" ,"orange",'cherry', 5, 45.9,True,"Akash" ]
print(mylist )

# used to add element
mylist.append("Karan") 
print(mylist)


# returns copy of list
mylist.copy()
print(mylist)


# returns no of elemnts
mylist.count("karan")
print(mylist) 


# returns index of element
mylist.index("orange")
print(mylist)   




# # remove all elemnts
# mylist.clear()

# insert at specific index  3 is index and 333333 is element
mylist.insert(3,333333)  
print(mylist)

# delete element at specific element
mylist.pop(3)  # 3 is index
print(mylist)

# # sort th list
# mylist.sort()
