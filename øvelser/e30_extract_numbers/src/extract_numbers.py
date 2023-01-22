#!/usr/bin/env python3

def extract_numbers(s):
    L = []
    for t in s.split():
        try:
            L.append(int(t))
        except ValueError:
            try:
                L.append(float(t))
            except ValueError:
                print(ValueError.args.count)
                continue
    return L

def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))

if __name__ == "__main__":
    main()
