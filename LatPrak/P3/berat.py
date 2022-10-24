arr = []
count = 0

# Input N
N = int(input())
arr.append(N)
while N != -999:
    N = int(input())
    if N != -999:
        arr.append(N)

if len(arr) != 0:
    # Validate Inputs
    validatedArr = []
    for i in range(len(arr)):
        if 30<= arr [i] <= 200:
            validatedArr.append(arr[i])

    if len(validatedArr) != 0:
        # Cek BB <= 50 or BB >= 100
        bb50 = 0 
        bb100 = 0
        for i in range(len(validatedArr)):
            if validatedArr[i] <= 50:
                bb50 += 1
            else:
                bb100 +=1

        print(len(validatedArr))
        print(bb50)
        print(bb100)
        print(round(sum(validatedArr) / len(validatedArr)))

    else:
        print('Data kosong')

else:
    print('Data kosong')