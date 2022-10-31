def jumlahderet(a):
    i = 1
    hasil = 0
    while i < a:
        hasil += i
        i += 2
    return hasil + a

a = int(input("batas : "))
print(f"Nilai jumlah deret adalah {jumlahderet(a)}")