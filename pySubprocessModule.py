import subprocess
p1=subprocess.Popen(["ping","www.google.com"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(p1)
print(type(p1))

output = p1.communicate()[0]
print("Output :", output)

error= p1.communicate()[1]
print("Error: ", error)


