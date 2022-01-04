runscored =1

def localFunction():
    runscored =2 #creates a new local object
    print("The value of runscored in localFunctions():", runscored)

def globalfunction():
    global  runscored
    runscored =3
    print("the value of runscored in globalfunction():",runscored)

print("the value of runscored in main: ", runscored)
localFunction()
print("After calling localFunction, the value of runscored in main: ", runscored)

globalfunction()
print("After calling globalFunction, the value of runscored in main: ", runscored)

localFunction()
print("After calling localFunction, the value of runscored in main: ", runscored)