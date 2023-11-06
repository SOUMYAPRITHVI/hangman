import random

def get_random_word(wordlist="/usr/share/dict/words"):
    good_words = []
    with open(wordlist) as f:
        words = [x.strip() for x in f]
        for word in words:
            if not word.isalpha(): # if there is punctuation
                continue
            if not word.islower(): # if it is a proper noun
                continue
            if len(word) < 5: # Too short
                continue
            good_words.append(word)

        return random.choice(good_words)
# def mask(word):
#     mask_word=""
#     for w in word:
#         mask_word+="-"
#     return mask_word
   

# def input_guessed_letter(target_word,masked_word ):
#     max_attempts=6
#     guessed_letters = set()
#     while True:
#         print(f"Word: {masked_word}")
#         print(f"Guessed letters: {', '.join(guessed_letters)}")
#         guess = input("Guess a letter: ").lower()

#         if len(guess) != 1 or not guess.isalpha():
#             print("Please enter a single letter.")
#             continue

#         if guess in guessed_letters:
#             print("You've already guessed this letter.")
#             continue

#         guessed_letters.add(guess)
#         if guess in target_word:
#             masked_word=guessed_word(target_word,guessed_letters)
#         else:
#             max_attempts-=1
#             print(f"Wrong guess! Attempts remaining: {max_attempts}")

#         if masked_word == target_word:
#             print(f"Word: {masked_word}")
#             print("Congratulations, you win!")
#             return "win"

#         if max_attempts==0:
#             print(f"Sorry, you lose! The word was '{target_word}'.")
#             return "lose"

def get_mask_word(target_word,guess):
    new_masked_word = ""
    for letter in target_word:
        if letter in guess:
            new_masked_word += letter
        else:
            new_masked_word += '-'
    return new_masked_word

