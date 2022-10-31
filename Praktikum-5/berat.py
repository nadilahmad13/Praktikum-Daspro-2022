# NAMA  : Ahmad Nadil
# NIM   : 16521516
# Judul : Menghitung Berat

# KAMUS

x = int(input())
rata = berat50 = berat100 = siswa = 0
while x != -999:
    if x >= 30 and x<= 200:
        siswa += 1
        if x <= 50:
            berat50 += 1
        elif x >= 100:
            berat100 += 1
        rata += x
    x = int(input())

if siswa == 0:
    print('Data kosong')
else:
    print(siswa)
    print(berat50)
    print(berat100)
    print(round(rata/siswa))