# NAMA  : Ahmad Nadil
# NIM   : 16521516
# Judul : Segitiga

# Program GambarSegitiga
# Input: N : integer
# Output: Jika N > 0 dan ganjil, gambar segitiga sesuai dengan N
#         Jika tidak, tampilkan pesan kesalahan: 

# KAMUS
# Variabel
#    N : int

def GambarSegitiga(N):
# I.S. N > 0 dan N ganjil
# F.S. Gambar belah ketupat dengan panjang diagonal mendatar sebesar N
#      sesuai spesifikasi soal
# Lengkapilah kamus lokal dan algoritma prosedur di bawah ini
    # Kamus Lokal
    #    x = integer
    #    y = integer

    # Algoritma
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

def IsValid(N):
# menghasilkan true jika N positif dan ganjil, false jika tidak
# Lengkapilah kamus lokal dan algoritma fungsi di bawah ini
    return (N > 0 and N % 2 != 0)

# INPUT
N = int(input())

if IsValid(N):
    GambarSegitiga(N)
else:
    print('Masukan tidak valid')