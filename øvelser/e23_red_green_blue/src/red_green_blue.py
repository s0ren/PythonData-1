#!/usr/bin/env python3

import re

def red_green_blue(filename="src/rgb.txt"):
    L = []

    with open(filename, 'r') as f:
        regex = r'(\d+)\s+(\d+)\s+(\d+)\s+(.*)$'
    #     L = [re.search(regex, line) for line in f]
    # L = ['\t'.join(m.groups()) for m in L if m]

        L = []
        for line in f:
            m = re.search(r'(\d+)\s+(\d+)\s+(\d+)\s+(.+)$', line )
            if m:
                g = m.groups()
                L.append('\t'.join(g))

        # L = []
        # for line in f:
        #     svar = re.findall(r'(\d+)\s+(\d+)\s+(\d+)\s+(.+)$', line )

        #     if svar:
        #         g = svar[0]
        #         L.append('\t'.join(g))
    return L


def main():
    print(red_green_blue(r'øvelser\e23_red_green_blue\src\rgb.txt'))

if __name__ == "__main__":
    main()
