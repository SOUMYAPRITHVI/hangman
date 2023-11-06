
import os
import hangman

def test_random_word_lowercase():
    # fname = "/usr/share/dict/words"
    fname = "/tmp/sample_wordlist"
    with open(fname, "w") as f:
        f.writelines(["Grape\n", "apple\n", "Mango\n"])
        
    for _ in range(100):
        assert hangman.get_random_word(fname) == "apple"

    os.unlink(fname)

def test_random_word_no_punctuation():
    fname = "/tmp/sample_wordlist"
    with open(fname, "w") as f:
        f.writelines(["pineapple\n", "mango's\n", '"beryl"'])

    for _ in range(100):
        assert hangman.get_random_word(fname) == "pineapple"

    os.unlink(fname)

def test_random_word_min_length_5():
    fname = "/tmp/sample_wordlist"
    with open(fname, "w") as f:
        f.writelines(["pineapple\n", "ape\n", 'dog\n', 'bear\n'])

    for _ in range(100):
        assert hangman.get_random_word(fname) == "pineapple"
        
    os.unlink(fname)


def test_random_word_no_repeated_words():
    words = {hangman.get_random_word() for _ in range(10)}
    assert len(words) == 10

def test_mask_word_no_guesses():
    word = "hangman"
    guesses = set()
    masked = hangman.get_mask_word(word, guesses)
    assert masked == "-------"

def test_mask_word_single_wrong_guess():
    word = "hangman"
    guesses = {"i"}
    masked = hangman.get_mask_word(word, guesses)
    assert masked == "-------"

def test_mask_word_single_correct_guess():
    word = "hangman"
    guesses =  {"m"}
    masked = hangman.get_mask_word(word, guesses)
    assert masked == "----m--"
def test_mask_word_two_correct_guesses():
    word = "hangman"
    guesses =  {"m","h"}
    masked = hangman.get_mask_word(word, guesses)
    assert masked == "h---m--"
def test_mask_word_single_guess_multiple_occurrence():
    word = "hangman"
    guesses =  {"m","h","a"}
    masked = hangman.get_mask_word(word, guesses)
    assert masked == "ha--ma-"

def test_get_status():
    secret_word = "hangman"
    turns_remain=6
    guesses =  ["h","m","a"]
    status = hangman.get_status(secret_word, turns_remain,guesses)
    assert status =="""Secret word : ha--ma- Turns remaining : 6 Guesses so far : hma"""

def test_play_round_crrect_guess():
    secret_word="rhino"
    turns_remain=5
    guesses={}
    guess='i'
    guesses,turns_remain,next_action=hangman.play_round(secret_word,turns_remain,guesses,guess)
    assert guesses=={'i'}
    assert turns_remain==4
    next_action="next"

