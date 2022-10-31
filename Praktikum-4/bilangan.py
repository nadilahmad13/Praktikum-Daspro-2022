# NAMA  : Ahmad Nadil
# NIM   : 16521516
# Judul : Bilangan

# Kamus
# N, X, temp = Integer
# arr = array of integer

# ALGORITMA
# Inisasi variabel
N = 0   # Nilai N
temp = 0    # temp digunakan untuk validasi angka yang di cek x
arr = []

# Looping untuk melakukan validasi terhadap nilai N
while not(0<N<=100):
    N = int(input())
    if not(0<N<=100):
        print('Masukan salah. Ulangi!')

# Looping untuk memasukkan nilai sebanyak N kali ke dalam array
for i in range(N):
    arr.append(int(input()))

X = int(input())    # Input nilai X

# Kondisi jika X = 0
if X == 0:
    # Looping untuk mengecek nilai 0 pertama dalam array
    for i in range(N):
        if arr[i] == 0:
            print(i+1)
            break
        else :
            temp += 1
    if temp == N: # jika temp telah mencapai N, maka dapat dipastikan seluruh array telah dicek
        print('Tidak ada 0')

# Kondisi jika X = -1 (Mencari nilai negatif)
elif X == -1:
    # Looping untuk mengecek nilai negatif pertama dalam array
    for i in range(N):
        if arr[i] < 0:
            print(i+1,arr[i])
            break
        else :
            temp += 1
    if temp == N: # jika temp telah mencapai N, maka dapat dipastikan seluruh array telah dicek
        print('Tidak ada negatif')

# Kondisi jika X = 1 (Mencari nilai positif)
elif X == 1:
    # Looping untuk mengecek nilai positif pertama dalam array
    for i in range(N):
        if arr[i] > 0:
            print(i+1,arr[i])
            break
        else:
            temp += 1
    if temp == N: # jika temp telah mencapai N, maka dapat dipastikan seluruh array telah dicek
        print('Tidak ada positif')

# Kondisi jika nilai X yang dimasukkan salah
else:
    print('Tidak diproses')