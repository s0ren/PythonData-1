#!/usr/bin/env python3

def sum_equation(L):
    # if len(L) == 0:
    if not L:
        equ = '0 = 0'
    else:
        s = str(sum(L))
        L = [str(k) for k in L]
        kvotienter = ' + '.join(L)
        equ = kvotienter + ' = ' + s
    return equ

def main():
    # print(sum_equation())
    print(sum_equation([]))
    print(sum_equation([1,2,3]))
    print(sum_equation([-5, 8, 117, -7, 77, 99]))

if __name__ == "__main__":
    main()
