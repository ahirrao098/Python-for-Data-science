#generates a list of number between 1 to 20 which are divisable by 3


result =[item for item in range(1,20)
    if item % 3 == 0 ]


print(result)