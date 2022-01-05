nums=range(1,11)
print("numbers:",nums)

even=lambda num: num % 2 == 0

print(even(5))
print(even(10))

result = filter(even,nums)
print("Result using filter - even :", result)
print("Type of result:", type(result))
print("List from result using filter - even:",list(result))

#=======================================

result = map(even,nums)
print("Result using map - even :", result)
print("Type of result:", type(result))
print("List from result using map - even:",list(result))#map takes the true false   & filter takes the exact input and generate the true value only