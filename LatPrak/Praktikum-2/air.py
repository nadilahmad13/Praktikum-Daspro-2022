def air(T):
    if T < 0:
        return "PADAT"
    elif 0 < T < 100:
        return "CAIR"
    elif T > 100:
        return "GAS"
    elif T == 0:
        return "ANTARA PADAT-CAIR"
    else:
        return "ANTARA CAIR-GAS"

T = int(input("T :"))
print(air(T))