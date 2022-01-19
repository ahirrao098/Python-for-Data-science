n=int(input())
result=[]
grade=[]
for i in range(n):
   name=(input())
   marks=float(input())
   result.append([name,marks])
   grade.append(marks)

print(result)
print(grade)

grade=sorted(set(grade))
print(grade)

m=grade[1]#need second lowest mark
print(m)

name=[]
for val in result:
   if m==val[1]:
      name.append(val[0])
print(name)

name.sort()
print(name)

for nm in name:
   print(nm)

