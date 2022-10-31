def max3bil(arr):
    return max(arr)

def max3bilold(a,b,c):
    if A > B and A > C:
        return A
    elif B > A and B > C:
        return B
    else:
        return C

arr = []
A = input("A :")
B = input("B :")
C = input("C :")

arr.append(A)
arr.append(B)
arr.append(C)

print(max3bil(arr))
print(max3bilold(A,B,C))