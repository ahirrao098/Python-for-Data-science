n = int(input())
    arr = map(int, input().split())

a=max(arr)

c=arr.count(a)
 for item in range(c):
     arr.remove(a)
     print(max(arr))