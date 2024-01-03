from words import words
import random
import string

def random_word():
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    
    return word.upper()

def hangman():
    print("Welcome To Hangman")
    word = random_word()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 7
    random_number = int(random.random() * len(word))
    # used_letters.add(word[random_number])

    while len(word_letters) > 0 and lives>0:
        word_list = [letter if letter in used_letters else "-" for letter in word]
        for x in used_letters:
            print(x)
        print("Current Lives : " , lives)
        print("current word:" , " ".join(word_list))
        used_letter = input("Input a letter : ").upper()

        print("\n")
        if used_letter in alphabet - used_letters:
            used_letters.add(used_letter)
            if used_letter in word_letters:
                word_letters.remove(used_letter)
            else:
                lives = lives - 1

        elif used_letter in used_letters:
            print("You already used this letter")
        else:
            print("Invalid Input, please try again.")
            
         
    print("The word was:{}".format(word))



hangman()