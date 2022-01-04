def myFunction():
    a="localvalue"
    print(a)
    print("Inside myFunction")


myFunction()
print(a)  ##Error ,the scope of a is within my function ...out side it is not run