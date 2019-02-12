
import argparse
import score_word

# Construct a list of possible words from sowpods.txt

with open("sowpods.txt","r") as infile:
    raw_input = infile.readlines()
    all_scrabble_words = [datum.strip('\n') for datum in raw_input]

# Get the word rack from the user in the command line

parser = argparse.ArgumentParser(description="Input a Scrabble Rack")
parser.add_argument('rack', help="Input rack")
args = parser.parse_args()
rack = (args.rack).upper()

# Check exceptions

if len(rack) < 2:
    raise Exception ("Cannot continue. A Scrabble word must be at least 2 letters.")
if len(rack) > 7:
    raise Exception ("Cannot continue. A Scrabble word must not be longer than 7 letters.")
for letter in rack:
    if letter not in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ?*"):
        raise Exception ("Cannot continue. Letters must be in the Roman alphabet or wildcards '?' or '*'.")


# # Find all valid words that can be made from the rack and put them in a separate list

valid_words = []

def valid_word(word, rack):
    available_letters = list(rack[:])
    blank_count = available_letters.count('*') + available_letters.count('?')

    missed_counter = 0
    for letter in word:
        if letter in available_letters:
            available_letters.remove(letter)
        else:
            missed_counter += 1

    if missed_counter <= blank_count:
        valid_words.append(word)

for word in all_scrabble_words:
    valid_word(word, rack)

# Score all words in the valid_words list, create tuples list of scores with respective words

tuples_list = []
available_letters = list(rack[:])
blank_count = available_letters.count('*') + available_letters.count('?')

for word in valid_words:
    if blank_count > 0:
        score_blanks = []
        for letter in word:
            if letter not in rack:
                score_blanks.append(score_word.score_word(letter))
            elif letter in rack:
                if word.count(letter) > rack.count(letter):
                    adjusted_letter_score = (word.count(letter) * score_word.score_word(letter)) - (rack.count(letter) * score_word.score_word(letter))
                    score_blanks.append(adjusted_letter_score)
                else:
                    continue
        score = score_word.score_word(word) - sum(score_blanks)
        tuples_list.append((score, word))
    else:
        score = score_word.score_word(word)
        tuples_list.append((score, word))

# Sort the list of tuples from largest to smalles

tuples_sorted = sorted(tuples_list, key=lambda tup: tup[0], reverse=True)

# print sorted list all possible words and their respective scores

print (*tuples_sorted, sep='\n')
print ("Total number of words: ", len(valid_words))
