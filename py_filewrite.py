#w==> write mode
#r==>read mode
#a==> Append mode

fh = open("FileExample.txt", "w")
print("file handle: ", fh)
print("Type of fh : ", type(fh))

fh.write("Welcome to file handling in Python .\n")
fh.write("This is second line .\n")
fh.write("Always close the file once the job is done .\n")

fh.close()