#!/usr/bin/env python3

def triple(x):
    return x*3

def square(x):
    return x**2

def main():
    ## part 1
    # for i in range(1, 10):
    #     print(f"triple({i})=={triple(i)} square({i})=={square(i)}")
    
    ## part 2, version 1
    # for i in range(1, 10):
    #     t=triple(i)
    #     s=square(i)
    #     if s > t:
    #         break
    #     print(f"triple({i})=={t} square({i})=={s}")

    ## part 2, version 2
    i = 1
    while (t:=triple(i)) >= (s:=square(i)):
        print(f"triple({i})=={t} square({i})=={s}")
        i += 1



if __name__ == "__main__":
    main()
