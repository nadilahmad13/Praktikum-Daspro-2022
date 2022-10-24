dataNilai = []

while True:
    angkaNilai = int(input())
    if angkaNilai == -9999:
        break
    elif 0 <= angkaNilai <= 100:
        dataNilai.append(angkaNilai)

if len(dataNilai) == 0:
    print('Data kosong')
else:
    # Banyak Mahasiswa
    print(len(dataNilai))

    # Nilai Lulus
    print(len([i for i in dataNilai if i >= 40]))

    # Nilai Tidak Lulus
    print(len([i for i in dataNilai if i < 40]))

    # Rata-Rata Berat
    rata = sum(dataNilai) / len(dataNilai)
    print("%.2f" % rata)