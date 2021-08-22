h, b, c, s = map(int, input().split())
store = h * b * c * s
total = store / 2**23

print(round(total, 1),'MB')