#!/usr/bin/env python3


def main():
    for y in range(1, 11):
        for x in range(1, 11):
            print(f"\t{x*y}", end="")
            #print(f"{x*y:4d}", end="")
        print()

if __name__ == "__main__":
    main()
