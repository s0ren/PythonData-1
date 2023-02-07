#!/usr/bin/env python3

def find_matching(L, pattern):
    R = []
    for i, w in enumerate(L):
        if pattern in w:
            R.append(i)
    return R

def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))

if __name__ == "__main__":
    main()
