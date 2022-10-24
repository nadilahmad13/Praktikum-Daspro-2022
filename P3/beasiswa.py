# NAMA  : Ahmad Nadil
# NIM   : 16521516
# Judul : Penentuan Beasiswa

ip = float(input())     # Input IP
pot = float(input())    # Input Pendapatan Orang Tua

# Algortima pengecekan IP dan Pendapatan Orang Tua
if ip >= 3.5:
    print(4)
elif pot < 1 and ip <3.5:
    print(1)
elif 1 <= pot < 5 and ip <3.5:
    if ip >= 2:
        print(3)
    else:
        print(2)
else:
    print(0)