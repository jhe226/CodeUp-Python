w, h, b = map(int, input().split())
store = w * h * b
total = store / 2**23

print('%.2f MB' % total)