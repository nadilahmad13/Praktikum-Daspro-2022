# NAMA  : Ahmad Nadil
# NIM   : 16521516
# Judul : Belah Ketupat

# Program BelahKetupat
# Input: N : integer
# Output: Jika N > 0 dan ganjil, gambar belah ketupat sesuai dengan N
#         Jika tidak, tampilkan pesan kesalahan: 

# KAMUS
# Variabel
#    N : int

def GambarBelahKetupat(N):
# I.S. N > 0 dan N ganjil
# F.S. Gambar belah ketupat dengan panjang diagonal mendatar sebesar N
#      sesuai spesifikasi soal
# Lengkapilah kamus lokal dan algoritma prosedur di bawah ini
    # Kamus Lokal
    #    x = integer
    #    y = integer

    # Algoritma
    x = N
    y = 1   # y bernilai 3 karena gambar bawah selalu diawali dengan tiga * simbol

    # Loop untuk membuat gambar bagian atas (sampai * (N-2) kali)
    while y < N:
        print(' '*((N-y)//2) + '*'*(y))
        y+=2
    
    # Loop untuk membuat gambar bagian bawah ( dari * N kali sampai akhir)
    while x >= 0:
        if x == N:
            print('*'*N)
            x-=2
        else:
            print(' '*((N-x)//2) + '*'*(x))
            x-=2

def IsValid(N):
# menghasilkan true jika N positif dan ganjil, false jika tidak
# Lengkapilah kamus lokal dan algoritma fungsi di bawah ini
    return (N > 0 and N % 2 != 0)

# INPUT
N = int(input())

if IsValid(N):
    GambarBelahKetupat(N)
else:
    print('Masukan tidak valid')