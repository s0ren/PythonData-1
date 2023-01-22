#!/usr/bin/env python3

def word_frequencies(filename='src/alice.txt'):
    with open(filename, 'r') as f:
        text = f.read()
    words = [w.strip("""!"#$%&'()*,-./:;?@[]_""") for w in text.split()]
    # words = [w.lower() for w in words]

    wc = {}
    for word in words:
        if word in wc.keys():
            wc[word] += 1
        else:
            wc[word] = 1

    # wc = {w: 0 for w in set(words)}
    # wc = {w: c + 1 for w, c in wc.items() }
    # for w in words:
    #     wc[w] += 1

    # print("the: ", wc['the'])

    wc = dict(sorted(wc.items(), key=lambda x: x[1], reverse=True))

    return wc

def main():
    print(word_frequencies(r'øvelser\e24_word_frequencies\src\alice.txt'))

if __name__ == "__main__":
    main()
