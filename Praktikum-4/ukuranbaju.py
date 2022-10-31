# NAMA  : Ahmad Nadil
# NIM   : 16521516
# Judul : Ukuran Baju

# ALGORITMA
t = int(input())
b = int(input())

# M = 1
# L = 2
# XL = 3
# undefined = 4

if t <= 150:
    print(1)
elif t > 170 and 60<b<=80:
    print(3)
elif 150<t<=170:
    if b<=80:
        print(2)
    elif b > 80:
        print(3)
else:
    print(4)