d = []
for _ in range(19):
    matrix = list(map(int, input().split()))
    d.append(matrix)

n = int(input())
for i in range(n):
  x, y = map(int, input().split())
  for j in range(19):
    if d[j][y-1] == 0:
      d[j][y-1] = 1
    else:
      d[j][y-1] = 0

    if d[x-1][j] == 0:
      d[x-1][j] = 1
    else:
      d[x-1][j] = 0

for y in d:
    print(*y)
