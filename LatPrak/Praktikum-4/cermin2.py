N = int(input())
for i in range(N,0,-2):
    if i == N:
        print('*'*N)
    else:
        print(' '*((N-i)) + '*'*(i))
        
for j in range(3,N+1,2):      
    if j == N:
        print('*'*N)
    else:
        print(' '*((N-j)) + '*'*(j))