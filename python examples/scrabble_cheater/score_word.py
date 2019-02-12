scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def score_word(word):
    total = 0
    for letter in word.lower():
        total += scores[letter]
    return total

# print (score_word("Today"))

# def score_word(score, words):
#     tupleslist = [(i, score(i)) for i in names]
#     tupleslist_sorted = sorted(tupleslist, key=lambda tup: tup[1], reverse=True)
#     justnames = [x[0] for x in tupleslist_sorted]
#     return justnames[0]
