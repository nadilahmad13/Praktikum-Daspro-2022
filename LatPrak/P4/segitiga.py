N = int(input())
x = N
y = 1

while y < N:
    print(' '*((N-y)) + '*'*(y))
    y+=2
    
while x >= 0:
    if x == N:
        print('*'*N)
        x-=2
    else:
        print(' '*((N-x)) + '*'*(x))
        x-=2