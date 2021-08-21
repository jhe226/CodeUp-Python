import sys

n = int(sys.stdin.readline().rstrip())

if n < 0:
    if abs(n) % 2 == 0:
        print('A')
    else:
        print('B')

else:
    if n % 2 == 0:
        print('C')
    else:
        print('D')