c, d= map(int, input().split())
C = bool(c)
D = bool(d)

print(((not C) and (not D)) or (C and D))