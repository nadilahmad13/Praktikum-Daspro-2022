# NAMA  : Ahmad Nadil
# NIM   : 16521516
# Judul : Gambar Pita

# Program GambarPita
# Input: N : integer
# Output: Jika N > 0 dan ganjil, gambar pita sesuai dengan N
#         Jika tidak, tampilkan pesan kesalahan: 

# KAMUS
# Variabel
#    N : int

def GambarPita(N):
# I.S. N > 0 dan N ganjil
# F.S. Gambar pita dengan lebar sebesar N sesuai spesifikasi soal
# Lengkapilah kamus lokal dan algoritma prosedur di bawah ini
    # Kamus Lokal
    #    x = integer
    #    y = integer

    # Algoritma
    x = N
    y = 3   # y bernilai 3 karena gambar bawah selalu diawali dengan tiga * simbol

    # Loop untuk membuat gambar bagian atas (sampai * satu kali)
    while x >= 0:
        if x == N:
            print('*'*N)
            x-=2
        else:
            print(' '*((N-x)//2) + '*'*(x))
            x-=2
            
    while y <= N:
        if y == N:
            print('*'*N)
            y+=2
        else:
            print(' '*((N-y)//2) + '*'*(y))
            y+=2

def IsValid(N):
# menghasilkan true jika N positif dan ganjil, false jika tidak
# Lengkapilah kamus lokal dan algoritma fungsi di bawah ini
    return (N > 0 and N % 2 != 0)

# INPUT
N = int(input())

if IsValid(N):
    GambarPita(N)
else:
    print('Masukan tidak valid')