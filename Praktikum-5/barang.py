# NAMA  : Ahmad Nadil
# NIM   : 16521516
# Judul : Menghitung Barang

# KAMUS
# N, total = integer

# ALGORITMA
N = int(input())
total = 0   # Inisiasi Variabel Temp
for i in range(N):  # Looping untuk input harga
    harga =int(input())
    total += harga  # Variabel total untuk menghitung harga total
print(total)