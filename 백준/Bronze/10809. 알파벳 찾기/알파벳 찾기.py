a = input()
arr = [-1]*26

for i in a:
    arr[ord(i)-97] = a.index(i)
print(*arr)
   