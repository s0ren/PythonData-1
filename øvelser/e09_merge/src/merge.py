#!/usr/bin/env python3

def merge(L1, L2):
    L = []
    i1 = 0
    i2 = 0
    while(i1 < len(L1) and i2 < len(L2)):
        if L1[i1] < L2[i2]:
            L.append(L1[i1])
            i1 += 1
        else:
            L.append(L2[i2])
            i2 += 1

    # resten
    # if i1 < len(L1):
    #     L.extend(L1[i1:])
    # else:
    #     L.extend(L2[i2:])

    L += L1[i1:] + L2[i2:]

    return L

def main():
    print(merge([1,2,4,7], [3,5,8,9]))

if __name__ == "__main__":
    main()
