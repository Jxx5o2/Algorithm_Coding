H, M = map(int, input().split())

if M < 45:
    if H == 0:
        print(23, 60-(45-M))
    else:
        print(H-1, 60-(45-M))
    
else:
    print(H, M-45)
