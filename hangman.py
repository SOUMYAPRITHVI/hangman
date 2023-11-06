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

def get_mask_word(target_word,guesses):
    new_masked_word = ""
    for letter in target_word:
        if letter in guesses:
            new_masked_word += letter
        else:
            new_masked_word += '-'
    return new_masked_word
def get_status(secret_word,turns_remain,guesses):
    masked_word=get_mask_word(secret_word,guesses)
    guesses = "".join(guesses)
    return f"""Secret word : {masked_word} Turns remaining : {turns_remain} Guesses so far : {guesses}"""

def play_round(secret_word,turns_remain,guesses,guess):
    if guess in guesses:
        return guesses,turns_remain,"next"
    guesses.append(guess)
    if "-" not in get_mask_word(secret_word,guesses):
        return guesses,turns_remain,"game_won" 
    if guess not in secret_word:
        turns_remain-=1
        if turns_remain==0:
            return guesses,turns_remain,"game_over"
    return guesses,turns_remain,"next"

def main():
    print ("Welcome to Hangman!")
    print ("-------------------\n\n")
    secret_word = get_random_word()
    print (secret_word)
    turns_remaining = 6
    guesses = []
    while True:
        status = get_status(secret_word, turns_remaining, guesses)
        print (status)
        guess = input("Enter your guess : ")
        guesses, turns_remaining, next_action = play_round(secret_word, turns_remaining,guesses, guess)
        if next_action == "game_over":
            print (f"You lost. The word is {secret_word}")
            break
        if next_action == "game_won":
            print (f"You won. The word is {secret_word}")
            break

if __name__ == "__main__":
    main()

# print(play_round("rhino",1,['r','n','o','h'],'i'))  
print(play_round("rhino",1,['s','w','u','m','y','a'],'x')) 
# print(get_status("hangman",6,{"m","h","a"}))