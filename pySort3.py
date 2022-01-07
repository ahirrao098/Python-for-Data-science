usrTuple=[9,5,4,6,3,2,1,8,7]

print("Original Tuple :", usrTuple)

s_list=sorted(usrTuple,reverse=True)#non place sorting

print("Sorted list:",(s_list))
print("Original list :", usrTuple)


#sorting using in built method
usrTuple.sort(reverse=True)#in place sorting
print("Original lst: ",usrTuple)