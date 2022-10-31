N = 0
temp = 0
while not(0<N<=100):
    N = int(input())
    if not(0<N<=100):
        print('Masukan salah. Ulangi!')
arr = []
for i in range(N):
    arr.append(int(input()))
X = int(input())

if X == 0:
    for i in range(N):
        if arr[i] == 0:
            print(i+1,arr[i])
            break
        else :
            temp += 1
    if temp == N-1:
        print('Tidak ada bilangan 0')

elif X == -1:
    for i in range(N):
        if arr[i] < 0:
            print(i+1,arr[i])
            break
        else :
            temp += 1
    if temp == N-1:
        print('Tidak ada negatif')

elif X == 1:
    for i in range(N):
        if arr[i] > 0:
            print(i+1,arr[i])
            break
        else:
            temp += 1
    if temp == N-1:
        print('Tidak ada positif')

else:
    print('Tidak diproses')