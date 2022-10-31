R1 = 0
R2 = 0
R3 = 0
pilihan = ''
hasil = 0
while not(R1 > 0 and R2 > 0 and R3 > 0 and (pilihan == 's' or pilihan == 'S' or pilihan == 'p' or pilihan == 'P')):
    R1 = float(input())
    R2 = float(input())
    R3 = float(input())
    pilihan = input()
    if not(R1 > 0 and R2 > 0 and R3 > 0 and (pilihan == 's' or pilihan == 'S' or pilihan == 'p' or pilihan == 'P')):
        print("Masukan salah")

if pilihan == 's' or pilihan == 'S':
    hasil = R1 + R2 + R3
else:
    hasil = 1 / (1 / R1 + 1 / R2 + 1 / R3)
print("%.2f" % hasil)