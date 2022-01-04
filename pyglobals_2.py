def myFunction():
    global temp
    temp="global variable"
    print("Value of temp INSIDE my function:",temp)

myFunction()#call my function if we used global variable yet
print("value of temp OUTSIDE myFunction:",temp)#error is showing without calling the "myFunction"...without function calling it will show error