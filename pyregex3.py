import re

s = '''
<html>
<head>
<title>
</title>
</head>
<body>
IP Adress are 172.45.78.109
LoopBack address:127.0.0.1
Computer 1:10.67.89.101
Computer 2:11.67.98.102
Computer 2:12.68.98.102

</body>
</html>
'''
print("Value of s: ", s)
lstValues=re.findall (r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",s)
print("Regex split using '\d'   : ", lstValues)

lstValues=re.findall (r"10\.\d{1,3}\.\d{1,3}\.\d{1,3}",s)
print("Regex split using '\d'   : ", lstValues)

lstValues=re.findall (r"[10|11|12]\.\d{1,3}\.\d{1,3}\.\d{1,3}",s)
print("Regex split using '\d'   : ", lstValues)