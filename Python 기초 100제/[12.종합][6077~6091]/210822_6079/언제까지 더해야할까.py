n = int(input())
s = 0
for i in range(n+1):
    s += i
    if s >= n:
        print(i)
        break