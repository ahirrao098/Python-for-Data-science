import sys

print("System platforms           : ", sys.platform)
print("System version             : ", sys.version)
print("System Version info        : ", sys.version_info)
print("Size of Int (Bytes)        :",sys.getsizeof(10))
print("Size of List (Bytes)       :",sys.getsizeof([]))
print("Size of Dict (Bytes)       :",sys.getsizeof({}))
print("Windows Version            :",sys.getwindowsversion())
print("System Path                :",sys.path)
print("System Recursion        : ", sys.getrecursionlimit())
