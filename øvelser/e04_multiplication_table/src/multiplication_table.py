#!/usr/bin/env python3


def main():
    for y in range(1, 11):
        for x in range(1, 11):
            print(f"{ x*y :>4d}", end=",")
            #print(" ", end="")
        print()

if __name__ == "__main__":
    main()
