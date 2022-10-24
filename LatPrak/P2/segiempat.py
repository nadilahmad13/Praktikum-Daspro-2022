def segiempat(N,C1,C2):
    if N > 0 and C1 != C2:
        temp = 1
        hasil = ""
        if temp == 1:
            for j in range(N):
                hasil += C1
            hasil += "\n"
            temp += 1

        while temp < N :
            for j in range(N):
                if j == 0 or j == N-1:
                    hasil += C1
                else:
                    hasil += C2

            hasil += "\n"
            temp += 1

        if temp == N:
            for j in range(N):
                hasil += C1
            hasil += "\n"
        return hasil

    else:
        return "Masukkan tidak valid"

N = int(input("N :"))
C1 = input("C1 :")
C2 = input("C2 :")
print(segiempat(N,C1,C2))