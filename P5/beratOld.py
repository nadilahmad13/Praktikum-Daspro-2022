# NAMA  : Ahmad Nadil
# NIM   : 16521516
# Judul : Menghitung Berat

# KAMUS
# N, mahasiswa, kurang50, lebih100, totalBerat = integer
# arr_berat = array of integer

# ALGORITMA
mahasiswa = 0
kurang50 = 0
lebih100 = 0
totalBerat = 0

N = int(input()) # Input N
while (N != -999):
    if 30 <= N <= 200: # Kondisi N yang valid akan dimasukkan ke dalam array
        mahasiswa += 1
        totalBerat += N
        if N <= 50:
            kurang50 += 1
        elif N >= 100:
            lebih100 += 1
    N = int(input())
    
if mahasiswa == 0:
    print('Data kosong')
else:
    print(mahasiswa)
    print(kurang50)
    print(lebih100)
    print(round(totalBerat/mahasiswa))