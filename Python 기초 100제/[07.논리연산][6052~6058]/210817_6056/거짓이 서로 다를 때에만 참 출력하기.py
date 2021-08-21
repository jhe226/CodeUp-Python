a, b = map(int, input().split())
A = bool(a)
B = bool(b)

print((A and (not B)) or ((not A) and B))