def gcd(a,m):
    while True:
        a = a % m
        a,m = m,a
        if m == 0:
            print(f'{a} is the gcd')
            break
gcd(12,5)