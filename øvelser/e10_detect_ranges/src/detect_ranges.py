#!/usr/bin/env python3

def detect_ranges(L):
    L = sorted(L)
    r = []

    i = 0
    b, e = None, None

    while i < len(L):
        if b is None:           # always a beginning
            b = i
        if i+1 < len(L):        # guard
            if L[i] == L[i+1]-1:
                e = i+1
            elif e is None:         # single
                r.append(L[b])
                b = None
            else:                   # interval
                r.append( (L[b], L[e]+1) )
                b, e = None, None
        i += 1
                                # remains
    if e is None:                   # single
        r.append(L[b])
    else:                           # interval
        r.append( (L[b], L[e]+1) )
        
    return r

def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13, 21 ]
    result = detect_ranges(L)
    print(L)
    print(result)

if __name__ == "__main__":
    main()
