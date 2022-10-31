#Pengisian array
N = int(input())
array = [0 for i in range(N)]

if N > 0 and N <= 100 :
    for i in range (N):
        array[i] =int(input())
else : 
    print("Masukan salah. Ulangi!")

#input X
X = int(input())

#Program Utama

if X == 0 :
    for i in range (N):
        if array[i] == 0 :
            print(str(i+1))
            break
        if i == N-1 :
            print ("Tidak ada 0")

elif X == (-1) :
    for i in range (N):
        if array[i] <0 :
            print(str(i+1) + " " + str(array[i]))
            break
        if i == N-1 :
            print ("Tidak ada negatif")

elif X == 1 :
    for i in range (N):
        if array[i] > 0:
            print(str(i+1) + " " + str(array[i]))
            break
        if i == N-1 :
            print ("Tidak ada positif")

else :
    print("Tidak diproses")