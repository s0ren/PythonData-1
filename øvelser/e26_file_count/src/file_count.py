#!/usr/bin/env python3

import sys

def file_count(filename='src/test.txt'):
    with open(filename, "r") as f:
        txt = f.read()
        lines = txt.count('\n')
        words = len(txt.split())
        chars = len(txt)
    return (lines, words, chars)

def main():
    for filename in sys.argv[1:]:
        print(*file_count(filename), filename, sep="\t" )

if __name__ == "__main__":
    main()
