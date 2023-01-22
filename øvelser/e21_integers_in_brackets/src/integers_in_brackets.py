#!/usr/bin/env python3

import re

def integers_in_brackets(s):
    res = re.findall(r'\[\s*([+-]?\d+)\s*\]', s)
    res = [int(m) for m in res]
    return res

def main():
    s = ' afd [asd] [12 ] [a34] [ -43 ]tt [+12]xxx'
    print(integers_in_brackets(s))

    s = ' afd [asd] [12 ] [a34] [\t +43 ]tt [-+12]xxx'
    print(integers_in_brackets(s))

if __name__ == "__main__":
    main()
