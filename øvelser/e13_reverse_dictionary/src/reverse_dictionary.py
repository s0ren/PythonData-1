#!/usr/bin/env python3

def reverse_dictionary(d):
    rd = {}
    # for key, values in d.items():
    #     for v in values:
    #         rd[v] = []
    # for key, values in d.items():
    #     for v in values:
    #         rd[v].append(key)
    for key, values in d.items():
        for v in values:
            if v not in rd:
                rd[v] = [key]
            else:
                rd[v] += [key]
    return rd

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
