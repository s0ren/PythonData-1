#!/usr/bin/env python3

def transform(s1, s2):
    l1 = list(map(int, s1.split()))
    l2 = list(map(int, s2.split()))
    print(l2)
    pairs = list(zip(l1, l2))
    print(pairs)
    prods = map(lambda p : p[0] * p[1], pairs )
    #prods = map(lambda x,y : x*y , l1, l2)
    return list(prods)

def main():
    print(transform("1 5 3", "2 6 -1"))

if __name__ == "__main__":
    main()
