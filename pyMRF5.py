from functools import reduce
#Reduce

nums=list (range(1,11))
print("Numbers:",nums)

addnos=lambda x,y : x+y
print(addnos(100,200))

result=reduce(addnos,nums)
print("result:",result)

multiply=lambda x,y : x*y
print(multiply(100,200))

result=reduce(multiply,nums)
print("result:",result)