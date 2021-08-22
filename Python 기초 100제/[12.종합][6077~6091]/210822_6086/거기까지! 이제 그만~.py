import sys
n = int(sys.stdin.readline().rstrip())
result = 0
for i in range(1, n+1):
    result += i
    if result >= n:
        break

print(result)