import random
from copy import deepcopy

with open("wordle-answers-alphabetical.txt") as fp:
    five_letter_words = [word.strip() for word in fp]

five_letter_words_set = set(five_letter_words)

answer = random.choice(five_letter_words).upper()

print("Welcome to our Wordle Game")

number_of_guesses = 0
max_number_of_guesses = 6

alphabet = {letter for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

alphabet_record = sorted(alphabet)
alphabet_sorted = alphabet_record.copy()
letters_correct = set()
letters_incorrect = set()

letter_count = {letter: 0 for letter in alphabet}
for letter in answer:
    letter_count[letter] += 1

RESET  = '\033[0m'

RED     = '\033[91m'
MAGENTA = '\033[95m'
GREEN   = '\033[92m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'

guesses = []

while True:

    # --- FIRST GET THE GUESS --- #
    guess = input("Guess a five letter word: ").upper()

    if guess == answer:
        print(f"You got it! The answer was {answer}")
        break

    # --- SECOND, CHECK IF THE GUESS IS VALID --- #

    guess_is_valid = True

    guess_is_five_letters = len(guess) == 5
    if not guess_is_five_letters:
        print("Your guess must be five letters long")
        guess_is_valid = False

    guess_is_all_letters = all(letter in alphabet for letter in guess)
    if not guess_is_all_letters:
        print("Your guess must only contain letters")
        guess_is_valid = False

    guess_is_a_valid_word = guess.lower() in five_letter_words_set
    if not guess_is_a_valid_word:
        print("Your guess is not a valid word")
        guess_is_valid = False

    if not guess_is_valid:
        print("Guess invalid, try again")
        continue

    # --- GUESS IS VALID BUT WRONG --- #

    print(f"Your guess was: {guess}")

    # --- BUILD UP THE HINT --- #

    guess_count = deepcopy(letter_count)
    hint = ["_"] * 5

    # --- first make a pass over the letters to find the exact matches
    for i, (lg, la) in enumerate(zip(guess, answer)):
        if lg == la: # if True
            hint[i] = GREEN + lg + RESET
            letters_correct.add(lg)
            guess_count[lg] -= 1

    # --- Now make a second pass to mark the letters that are correct but in the wrong place
    for i, (lg, la) in enumerate(zip(guess, answer)):
        if lg == la:
            continue  # we saw this one already
        elif guess_count[lg] > 0:
            hint[i] = BLUE + lg + RESET
            letters_correct.add(lg)
            guess_count[lg] -= 1
        else:
            letters_incorrect.add(lg)

    # --- SHOW ALPHABET GUESS RECORD --- #

    guesses.append("".join(hint))
    for g in guesses:
        print(g)

    for i, letter in enumerate(alphabet_sorted):
        if letter in letters_correct:
            alphabet_record[i] = "\u001b[42;37m\u001b[42m\u001b[30m" + letter + RESET
        elif letter in letters_incorrect:
            alphabet_record[i]   = RED + letter + RESET

    print("".join(alphabet_record))

    # correct_letters = [letter for letter in guess if letter in answer]
    # wrong_letters = [letter for letter in guess if letter not in answer]
    # print("Correct letters: ", correct_letters)
    # print("Incorrect letters: ", wrong_letters)

    number_of_guesses += 1

    if number_of_guesses >= max_number_of_guesses:
        print(f"Sorry, the answer was: {answer}")
        break

    print(f"number of guesses remaining: {max_number_of_guesses - number_of_guesses}")
