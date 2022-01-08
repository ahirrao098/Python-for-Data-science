#Sorting based on keys param
usrlist = [9, 4, -2, 1, 5, 3, 6, -8, 7]

print("Original list: ", usrlist)

slist=sorted(usrlist, key=abs)

print("Sorted list :", slist)
print("Original list: ", usrlist)