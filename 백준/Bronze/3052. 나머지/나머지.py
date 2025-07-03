a = []
for i in range(10):
    N = int(input())
    a.append(N)

b = []
for j in a:
    b.append(j%42)

b = set(b)

print(len(b))
    

    


    
