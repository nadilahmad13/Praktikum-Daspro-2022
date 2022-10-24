# NAMA  : Ahmad Nadil
# NIM   : 16521516
# Judul : Segiempat

# Input
N = int(input())
C1 = input()
C2 = input()

# Algoritma
if not (N > 0 and C1 != C2):
    print('Masukan tidak valid')
else:
    for i in range(N):
        # Kondisi untuk baris pertama dan terakhir
        if i == 0 or i == N-1:
            print(C1*N)

        # Kondisi untuk baris di tengah
        else:
            print(C1 + (N-2)*C2 + C1)