#!/usr/bin/env python3

def merge(L1, L2):
    L = []
    p1 = p2 = 0
    while p1 < len(L1) and p2 < len(L2):
        if L1[p1] < L2[p2]:
            L.append(L1[p1])
            p1 += 1
        else:
            L.append(L2[p2])
            p2 += 1
    # sidsten
    if p1 < len(L1):
        L.extend(L1[p1:])
    else:
        L.extend(L2[p2:])
    
    return L

def main():
    L1 = [1,2,5,13,22]
    L2 = [3,6,8,15,42]
    print(merge(L1, L2))

    L1 = [1,2,5,13,22, 55]
    L2 = [1, 3,15,42]
    print(merge(L1, L2))

    L1 = sorted([6,4,7,37,35689,46784678,4356,-6])
    L2 = sorted([3457,478,54769,57,9,-45673,5476,567,3567,657])
    print(merge(L1, L2))


if __name__ == "__main__":
    main()
