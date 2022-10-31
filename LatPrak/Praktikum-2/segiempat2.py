n = int(input())
c1 = input()
c2 = input()

if n <= 0 or c1 == c2:
    print("Masukan tidak valid")
else:
    for i in range(n):
        if i == 0 or i == n-1: print(n*c1)
        else:
            print(c1 + (n-2)*c2 + c1)