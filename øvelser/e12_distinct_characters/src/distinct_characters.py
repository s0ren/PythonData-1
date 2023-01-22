#!/usr/bin/env python3

def distinct_characters(L):
    unique_dict = {}
    print(set(L))
    for word in L:
        s = len(set(word))
        unique_dict[word] = s
    return unique_dict

def main():
    print(distinct_characters(["check", "look", "try", "pop"]))

if __name__ == "__main__":
    main()
