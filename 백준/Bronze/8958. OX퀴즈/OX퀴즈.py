N = int(input())

for i in range(N):
    a = list(input())
    ans = 0
    count = 0
    for i in a:
        if i == 'O':
            count += 1
            ans += count
        else:
            count = 0
    print(ans)