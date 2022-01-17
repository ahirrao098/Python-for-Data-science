import os

print(os.getcwd())

if os.path.exists("test"):
    print("Directory already exists")

else:
    os.mkdir("test")