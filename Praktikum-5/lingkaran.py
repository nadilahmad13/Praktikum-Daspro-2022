# NAMA  : Ahmad Nadil
# NIM   : 16521516
# Judul : Mencari Luas Lingkaran

# KAMUS
# r = float

r = int(input())

if r <= 0:
    print("Jari-jari harus > 0")
else:
    luas = 3.1415 * r * r
    print("%.2f" % luas)