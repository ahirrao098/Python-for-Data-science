# take a sequence of numbers from the user
# 1st number:Count
#2nd..Count:all are numbers

#5 1 2 3 4 5
#35 10 45 76  3 4
# 3 100 45 60

usrInput=input(" ")
print(usrInput)

lstNos= list(map(int, usrInput.split()))

print("list of numbers: ", lstNos)

avg=sum(lstNos[0:]) / lstNos[0]
print(avg)