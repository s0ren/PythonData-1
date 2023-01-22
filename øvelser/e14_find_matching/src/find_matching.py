#!/usr/bin/env python3

def find_matching(L, pattern):
    res = []
    for i, k in enumerate(L):
        if pattern in k:
            res.append(i)
    return res

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment", "skinke", 'pølsen'], "en"))

if __name__ == "__main__":
    main()
