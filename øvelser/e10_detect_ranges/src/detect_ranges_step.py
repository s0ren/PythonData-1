#!/usr/bin/env python3

def detect_ranges(L):
    L = sorted(L)
    res = []

    begin  = None
    end    = None
    p      = 0
    while p < len(L) -1:
        if begin is None:
            begin = L[p]
        if L[p+1] - L[p] == 1:              # Hvis næste element er præcis 1 større
            end = L[p+1]                    # er der et interval (som måske er længere...)
        elif end is None:                   # så er der en single i begin
            res.append(begin)                   # tilføj singlen
            begin = None
        else:                               # så er intervallet slut
            res.append( (begin, end+1) )        # tilføj et interval som par
            begin = None
            end = None
        p += 1

    return res

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    #   [2, 4, 5, 6, 7, 8, 10, 12, 13]
    result = detect_ranges(L)
    print(L)
    print(result)

    L = [1,2,4] # single sidst
    print(L)
    print(detect_ranges(L))

if __name__ == "__main__":
    main()
