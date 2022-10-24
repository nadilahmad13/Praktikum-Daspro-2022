# NAMA  : Ahmad Nadil
# NIM   : 16521516
# Judul : Konversi Suhu

# ALGORITMA
t = float(input())  # Besar suhu (Celcius)
k = input()         # Suhu tujuan

if k == 'R':
    print("%.2f" % ((4/5) * t))
elif k == 'F':
    print("%.2f" % ((9/5) * t + 32))
elif k == 'K':
    print("%.2f" % (t + 273.15))