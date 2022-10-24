# NAMA  : Ahmad Nadil
# NIM   : 16521516
# Judul : Menghitung Nilai

# ALGORITMA
mahasiswa = 0
lulus = 0
tidaklulus = 0
totalNilai = 0

N = int(input()) # Input N
if N == -9999:
    print('Data nilai kosong')
else:
    while N != -9999:
        if N >= 0 and N <= 100: # Kondisi N yang valid akan dimasukkan ke dalam array
            mahasiswa += 1
            totalNilai += N
            if N < 40:
                tidaklulus += 1
            elif N >= 40:
                lulus += 1
        N = int(input())
        
    if mahasiswa == 0:
        print(0)
    else:
        print(mahasiswa)
        print(lulus)
        print(tidaklulus)
        rata = totalNilai/mahasiswa
        print("%.2f" % rata)