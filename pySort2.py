usrlist=[9,5,4,6,3,2,1,8,7]

print("Original list :", usrlist)

s_list=sorted(usrlist,reverse=True)#non place sorting

print("Sorted list:",s_list)
print("Original list :", usrlist)


#sorting using in built method
usrlist.sort(reverse=True)#in place sorting
print("Original lst: ",usrlist)