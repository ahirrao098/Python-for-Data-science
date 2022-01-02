#Given the subjects= "MATHEMATICS ", print all the consonants in a list
#['M','T','H','M','T','C','S']

result=[]
for item in "MATHEMATICS":
    if item not in "AEIOU":
        result.append(item)

print(result)

#same in list comrehension

result=[item for item in "MATHEMATICS" if item not in "AEIOU"]
print(result)