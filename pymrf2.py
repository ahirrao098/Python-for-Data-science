nums=list(range(1,12))
print("numbrs :", nums)

sq=lambda num:num * num

mobject=map(sq,nums)
print(mobject)
print(type(mobject))

print("list of square of nums using Map:",list(mobject))
#print("tuple of square of nums using Map:",tuple(mobject)) #only one can be generate output ..either list or tuple