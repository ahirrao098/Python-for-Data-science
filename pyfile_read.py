fh = open("FileExample.txt")# default mode is read mode

strContents = fh.read()

fh.close()

print("File content: ",strContents)
print("Type of strContents: ",type(strContents))
