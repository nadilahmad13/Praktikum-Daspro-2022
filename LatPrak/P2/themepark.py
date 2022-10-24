t = int(input())
b = int(input())
k = int(input())

temp_k = []

if t > 100 and 0 < b <=150:
    temp_k.append(2)
    temp_k.append(3)
    temp_k.append(4)
elif 0 < t <= 100 and 30 < b <= 150:
    temp_k.append(1)
    temp_k.append(2)
elif 0 < t <= 100 and 0 < b <= 150:
    temp_k.append(1)
elif 0 < t <= 100 and b > 150:
    temp_k.append(2)
elif 100 < t <= 200 and b > 150:
    temp_k.append(2)
    temp_k.append(3)

if len(temp_k) > 0:
    for i in range (len(temp_k)):
        if temp_k[i] == k:
            print('TRUE')
            break
        elif i == len(temp_k)-1:
            print('FALSE')

elif len(temp_k) == 0 and k == 0:
    print('TRUE')
elif len(temp_k) == 0 and k != 0:
    print('FALSE')
else: 
    print('FALSE')