N = int(input())
upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
symbols = {'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
while not(0<N<=100):
    print('Masukan salah, Ulangi!')
    N = int(input())
arr = []
for i in range(N):
    arr.append(input())
cc = input()
temp = 0
if cc == 'S' or cc == 's':
    for i in range(len(arr)):
        for j in range(len(lower)):
            if arr[i] == lower[j] and temp == 0:
                print(f"{i+1} {arr[i]}")
                temp += 1
                break
    if temp == 0:
        print('Tidak ada huruf kecil')

elif cc == 'L' or cc == 'L':
    for i in range(len(arr)):
        for j in range(len(upper)):
            if arr[i] == upper[j] and temp == 0:
                print(f"{i+1} {arr[i]}")
                temp += 1
                break
    if temp == 0:
        print('Tidak ada huruf besar')

elif cc == 'X' or cc == 'x':
    for i in range (len(arr)):
        for j in range(len(symbols)):
            if arr[i] == symbols[j] and temp == 0:
                print(f"{i+1} {arr[i]}")
                temp += 1
                break
    if temp == 0:
        print('Semua Huruf')

else:
    print('Tidak diproses')