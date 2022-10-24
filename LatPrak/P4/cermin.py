N = int(input())
x = N
y = 3
while x >= 0:
    # for i in range(N,0,-2):
    if x == N:
        print('*'*N)
        x-=2
    else:
        print(' '*((N-x)) + '*'*(x))
        x-=2
        
while y <= N:
    if y == N:
        print('*'*N)
        y+=2
    else:
        print(' '*((N-y)) + '*'*(y))
        y+=2