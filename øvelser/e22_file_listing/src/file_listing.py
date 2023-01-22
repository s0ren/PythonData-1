#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):
    L = []

    with open(filename, 'r') as f:
        for line in f:
            r = re.findall(r'\s+(\d+)\s(\w{3})\s+(\d{1,2})\s+(\d{2}):(\d{2})\s([\w\.]+)', line)
            r = r[0]
            res = (int(r[0]), r[1], int(r[2]), int(r[3]), int(r[4]), r[5]) 
            L.append(res)
    return L

def main():
    print(file_listing('øvelser\e22_file_listing\src\listing.txt'))

if __name__ == "__main__":
    main()
