N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))
X = int(input())
if X in arr:
    if X == max(arr):
        print('maksimum')
    if X == min(arr):
        print('minimum')
    if X != max(arr) and X != min(arr):
        print('N#A')
else:
    print(X,'tidak ada')