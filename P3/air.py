# NAMA  : Ahmad Nadil
# NIM   : 16521516
# Judul : Penentuan Fasa Air

T = int(input())

if T < 0:
    print('PADAT')
elif 0 < T < 100:
    print('CAIR')
elif T > 100:
    print('GAS')
elif T == 0:
    print('ANTARA PADAT-CAIR')
else:
    print('ANTARA CAIR-GAS')