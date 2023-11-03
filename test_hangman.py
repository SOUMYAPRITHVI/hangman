
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

def test_mask():
    word = "hangman"
    assert hangman.mask(word)=="-------"


def test_win_guessed_letter():
    # Test case 1: No guessed letters
    word = "hangman"
    guessed_letters = set()
    masked = hangman.guessed_word(word, guessed_letters)
    assert masked == "-------"
    # , f"Expected: '-------', Got: '{masked}'"

    # Test case 2: Some guessed letters
    word = "hangman"
    guessed_letters = {"h", "n", "g", "m", "i"}
    masked = hangman.guessed_word(word, guessed_letters)
    assert masked == "h-ngm-n"
    # f"Expected: 'pr-g--mmi-', Got: '{masked}'"

def test_lose_guessed_letter():
    # Test case 1: No guessed letters
    word = "hangman"
    guessed_letters =  {"e", "s", "d", "x", "i","r"}
    masked = hangman.guessed_word(word, guessed_letters)
    assert masked == "-------"
    

