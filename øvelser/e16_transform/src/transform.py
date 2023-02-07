#!/usr/bin/env python3

from functools import reduce

def transform(s1, s2):
    z = list(zip(s1.split(), s2.split()))
    print(z)
    # L = list(map(lambda t : int(t[0]) * int(t[1]), z))
    L = list(map(lambda t : reduce(lambda i, j : int(i) * int(j), t), z))
    return L

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
