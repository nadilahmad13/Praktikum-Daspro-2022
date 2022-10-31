list = []
lulus = 0
tidak_lulus = 0
total = 0
temp = 0
valid = 0

while True:
    nilai = int(input())
    if nilai == -9999:
        break
    else:
        temp += 1
        if nilai >= 0 and nilai <= 100:
            valid += 1
            list.append(nilai)
            if nilai >= 40:
                lulus += 1
            elif nilai < 40:
                tidak_lulus += 1
            total += nilai

if len(list) == 0 and temp == 0:
    print('Data nilai kosong')

elif len(list) == 0 and temp != 0:
    print(0)
    
else:
    print(valid)
    print(lulus)
    print(tidak_lulus)
    print(total)
    print("%.2f" % (total/valid))