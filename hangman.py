#This function displays the state of the word to be guessed.
def displayword(word, guessedletters):
    return ' '.join([letter if letter in guessedletters else '_' for letter in word])
    #This is the main function for the game.
def hangman():
    print("Welcome to the game!!!")
    guessedletters = set()
    wordchosen = chooseword()
    chances = 6
    while chances > 0 :
        print("Word : ",displayword(wordchosen, guessedletters))
        print("Remaining chances : ", chances)
        print(f"Guessed Letters : {' '.join(sorted(guessedletters)) if guessedletters else 'None'}")
        
        guess = input('Enter the next guess : ').lower() #Makes all guesses in lower.
        
        if len(guess) != 1 or not guess.isalpha() : #Checks for valid inputs.
            print("The guess was not appropriate. Please enter a single letter as your guess.")
            continue

        if guess in guessedletters : #Checks whether the letter has already been guessed.
            print("You have already guessed this letter please try again")
            continue

        guessedletters.add(guess) #Adds the letter to the set of guessed letters.

        if guess in wordchosen:
            print("Good job! You guessed a letter correctly.")
            if set(wordchosen) <= set(guessedletters):
                print("Congratulations! You've guessed the word:", wordchosen)
                break

        else:
            print("Oops! That letter is not in the word. Try Again")
            chances-=1

    if chances == 0 :
        print("Gameover. You have lost the game. The word was", wordchosen, ". Better luck next time.")

    
    
