n = int(input())
arr = input().split()
d = []

for i in range(n):
    arr[i] = int(arr[i])

for i in range(24) :
    d.append(0)

for i in range(n):
    d[arr[i]] += 1

for i in range(1, 24):
    print(d[i], end = ' ')