# NAMA  : Ahmad Nadil
# NIM   : 16521516
# Judul : Mencari Karakter

# KAMUS
# N = integer
# arr = array of characters
# cc = string

# Algoritma
while True: # Validasi Input N
    N = int(input())
    if 0 < N <= 100:
        break
    else:
        print('Masukan salah. Ulangi!')

arr = []    # Inisialisasi array kosong

for i in range(N):  # Looping isi array
    arr.append(input())

cc = input() # Input Kondisi

# Array berisi huruf besar dan huruf kecil
upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

count = 0 # Inisiasi counter

if cc == 's' or cc == 'S':
    for i in range(N):
        count += 1
        if arr[i] in lower:
            print(i+1,arr[i])
            break
        if count == N:
            print('Tidak ada huruf kecil')
            break

elif cc == 'l' or cc == 'L':
    for i in range(N):
        count += 1
        if arr[i] in upper:
            print(i+1,arr[i])
            break
        if count == N:
            print('Tidak ada huruf besar')
            break

elif cc == 'x' or cc == 'X':
    for i in range(N):
        if arr[i] not in upper and arr[i] not in lower:
            if count == 0:
                save = arr[i]
                index = i+1
            count += 1
    if count == 0:
        print("Semua huruf")
    else:
        print(index,save)

else:
    print('Tidak diproses')