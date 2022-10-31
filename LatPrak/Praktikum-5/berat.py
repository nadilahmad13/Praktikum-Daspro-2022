arr_berat = []

while True:
    N = int(input())
    if N == -999:
        break
    elif 30 <= N <= 200:
        arr_berat.append(N)

if len(arr_berat) == 0:
    print('Data kosong')
else:
    # Banyak Mahasiswa
    print(len(arr_berat))

    # Berat <= 50
    print(len([i for i in arr_berat if i <= 50]))

    # Berat >= 100
    print(len([i for i in arr_berat if i >= 100]))

    # Rata-Rata Berat
    print(round(sum(arr_berat) / len(arr_berat)))