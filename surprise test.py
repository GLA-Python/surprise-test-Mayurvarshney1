def check(a):
    for i in range(len(a)):
        x = a[i]-a[i-1]
        y = a[i-1]-a[i-2]
        if x**2 > y**2:
            p = True
        else:
            p = False
    return p
n = list(map(int, input().split()))
m = check(n)
print(m)
