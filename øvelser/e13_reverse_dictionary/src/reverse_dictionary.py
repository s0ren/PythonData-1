#!/usr/bin/env python3

def reverse_dictionary(d):
    rd = {}
    for eng_word in d.keys():
        #print('eng:', eng_word, 'finsk:', d[eng_word])
        for fin_word in d[eng_word]:
            print('e:', eng_word, 'fin_word:', fin_word)
            if fin_word in rd:
                rd[fin_word].append(eng_word)
            else:
                rd[fin_word] = [eng_word]
    return rd

def main():
    d={'move': ['liikuttaa'], 'hide': ['piilottaa', 'salata'], 'six': ['kuusi'], 'fir': ['kuusi']}
    print(reverse_dictionary(d))

if __name__ == "__main__":
    main()
