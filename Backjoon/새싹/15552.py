import sys
t = int(input())

for o in range(t):
    a, b = sys.stdin.readline().rstrip().rsplit()
    b = int(b)
    a = int(a)
    print(a+b)
