a = int(input())
b = list(input())
b.reverse()

for i in b:
    print(a*int(i))
    
b.reverse()
c = int(''.join(b))
print(a*c)
