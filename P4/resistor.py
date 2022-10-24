# NAMA  : Ahmad Nadil
# NIM   : 16521516
# Judul : Menghitung Hambatan Total

# Kamus
# R1,R2,R3,Rt = Float (real)
# pilihan = string

# Inisiasi Nominal Awal
R1 = 0  # Hambatan 1
R2 = 0  # Hambatan 2
R3 = 0  # Hambatan 3
pilihan = ''    # Pilihan
Rt = 0  # Hambatan Total

# Looping untuk memvalidasi serta melakukan input R1, R2, dan R3
while not(R1 > 0 and R2 > 0 and R3 > 0 and (pilihan == 's' or pilihan == 'S' or pilihan == 'p' or pilihan == 'P')):
    R1 = float(input())
    R2 = float(input())
    R3 = float(input())
    pilihan = input()

    # Kondisi untuk mengirim pesan kesalahan jika input masih salah
    if not(R1 > 0 and R2 > 0 and R3 > 0 and (pilihan == 's' or pilihan == 'S' or pilihan == 'p' or pilihan == 'P')):
        print("Masukan salah")

# Perhitungan Hambatan total (Rt) jika pilihan merupakan rangkaian seri
if pilihan == 's' or pilihan == 'S':
    Rt = R1 + R2 + R3

# Perhitungan Hambatan total (Rt) jika pilihan merupakan rangkaian paralel
else:
    Rt = 1 / (1 / R1 + 1 / R2 + 1 / R3)

# Output akhir dengan format 2 angka desimal
print("%.2f" % Rt)