#!/usr/bin/env python3

def interleave(*lists):
    L = []
    L2 = []
    # print(*lists)
    z = list(zip(*lists))
    # print(z)
    
    for t in z:
        # print(t)
        L.extend(t)
        L2.append(t)
        print('L2:', L2)
        # print('L:', L)

    return L

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
