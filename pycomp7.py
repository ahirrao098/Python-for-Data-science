alphabets=["a","b","c","d"]
fruits=["apple","banana","mango","cherry"]

#{'a'=('apple',5)'b':('banana',6)..}

result={alphabets[item]:(fruits[item],len(fruits[item]) )for item in range(0,4)}

print(result)