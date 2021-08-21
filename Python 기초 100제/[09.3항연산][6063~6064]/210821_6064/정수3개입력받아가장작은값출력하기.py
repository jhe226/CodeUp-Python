a, b, c = map(int, input().split())
d = a if a < b else b
print(d if d < c else c)