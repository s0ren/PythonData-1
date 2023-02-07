#!/usr/bin/env python3

def interleave(*lists):
    z = list(zip(*lists))
    print("zipped:", z)
    L = []
    for t in z:
        L.extend(t)
    return L

def main():
    print(interleave([1, 2, 3], [20, 30, 40], ['a', 'b', 'c']))

if __name__ == "__main__":
    main()
