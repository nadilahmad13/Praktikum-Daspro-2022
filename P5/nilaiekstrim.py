# NAMA  : Ahmad Nadil
# NIM   : 16521516
# Judul : Menghitung Nilai Ekstrim

# KAMUS
# N = integer
# arr = array of integer

# ALGORITMA
N = int(input())    #Input N
arr = []    # Inisialisasi array kosong

for i in range(N):  # Looping input array sebanyak N kali
    arr.append(int(input()))

X = int(input())    # Input Angka X untuk di cek

if X in arr:    # Kondisi untuk cek apakah X ada pada array
    if X == max(arr):
        print('maksimum')
    if X == min(arr):
        print('minimum')
    if X != max(arr) and X != min(arr):
        print('N#A')
else:
    print(X,'tidak ada')