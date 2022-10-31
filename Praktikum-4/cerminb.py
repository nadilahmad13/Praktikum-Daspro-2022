# NAMA  : Ahmad Nadil
# NIM   : 16521516
# Judul : CerminB

# Program GambarBTercermin
# Input: N : integer
# Output: Jika N > 0 dan ganjil, gambar B tercermin sesuai dengan N
#         Jika tidak, tampilkan pesan kesalahan: 

# KAMUS
# Variabel
#    N : int

def GambarBTercermin(N):
# I.S. N > 0 dan N ganjil
# F.S. Gambar B tercermin dengan lebar sebesar N sesuai spesifikasi soal
# Lengkapilah kamus lokal dan algoritma prosedur di bawah ini
    # Kamus Lokal
    #    x = integer
    #    y = integer

    # Algoritma
    x = N
    y = 3   # y bernilai 3 karena gambar bawah selalu diawali dengan tiga * simbol

    # Loop untuk membuat gambar bagian atas (sampai * satu kali)
    while x >= 0:
        if x == N:  # Line paling atas
            print('*'*N)
            x-=2
        else: # Line setelahnya
            print(' '*((N-x)) + '*'*(x))
            x-=2

    # Loop untuk membuat gambar bagian bawah ( dari * tiga kali sampai akhir)           
    while y <= N:
        if y == N: # Line paling bawah
            print('*'*N)
            y+=2
        else: # Line sebelum paling bawah
            print(' '*((N-y)) + '*'*(y))
            y+=2

def IsValid(N):
# menghasilkan true jika N positif dan ganjil, false jika tidak
# Lengkapilah kamus lokal dan algoritma fungsi di bawah ini
    return (N > 0 and N % 2 != 0)

# INPUT
N = int(input())

if IsValid(N):
    GambarBTercermin(N)
else:
    print('Masukan tidak valid')