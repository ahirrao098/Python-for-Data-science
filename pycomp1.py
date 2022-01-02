#Approch 1

result=[]
for item in range(1,13):
    result.append(item*item)

print(result)

#Approch 2:
result=[item*item for item in range(1,13)]
print(result)

#Approch 2:
print([item*item for item in range(1,13)])