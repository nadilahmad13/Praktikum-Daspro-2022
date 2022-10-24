arr = [2,1,3,4,6,12,3,6]
minimums = arr[0]
for i in range(len(arr)):
    if arr [i] < minimums:
        minimums = arr[i]
print(minimums)