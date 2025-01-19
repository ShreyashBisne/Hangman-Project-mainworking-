import random
def chooseword():
    words = ["shreyash", "aryan", "aman", "parth", "rehan"]
    return random.choice(words)


def displayword(word, guessedletters):
    return ' '.join([letter if letter in guessedletters else '_' for letter in word])
    
def hangman():
    print("Welcome to the game!!!")
    guessedletters = set()
    wordchosen = chooseword()
    chances = 6
    while chances > 0 :
        print("Word : ",displayword(wordchosen, guessedletters))
        print("Remaining chances : ", chances)
        print(f"Guessed Letters : {' '.join(sorted(guessedletters)) if guessedletters else 'None'}")
        
        guess = input('Enter the next guess : ').lower()
        
        if len(guess) != 1 or not guess.isalpha() :
            print("The guess was not appropriate")
            continue

        if guess in guessedletters :
            print("You Dumb")
            continue

        guessedletters.add(guess)

        if guess in wordchosen:
            print("Good job! You guessed a letter correctly.")
            if set(wordchosen) <= set(guessedletters):
                print("Congratulations! You've guessed the word:", wordchosen)
                break

        else:
            print("Oops! That letter is not in the word.")
            chances-=1

    if chances == 0 :
        print("gameover")

    
    
