# Hangman-Project-mainworking-
The project begins with the understanding for the entire flow for the code for which one needs to develop and understand the pseudo-code for the program.

The following is the pseudo-code that I developed for the main function of the game :0

**Step 1 : Function** display_word(word, guessed_letters):

- Initialize an empty string for the displayed word.
- For each letter in the word:
    - If the letter is in guessed_letters:
        - Add the letter to the displayed word.
    - Else:
        - Add an underscore (_) to the displayed word.
- Return the displayed word.

**Step 2 : Function** hangman():

Initiate the function by declaring variables, messages, etc.

- Print a welcome message.
- Call choose_word() to select a word to guess.
- Initialize an empty set guessed_letters.
- Set attempts to 6.

Set up the iterations that will be required to iterate through the word,attempts available and the letters guessed in each step.

**While attempts > 0:**

- Print the current word by calling display_word() with word and guessed_letters.
- Print the number of remaining attempts.
- Print the list of guessed letters (or "None" if the set is empty).

Take an input from the user in each iteration.

- Input guess from the player.
    - Convert the guess to lowercase.(Understand the importance of this step as we know that python is strict about it’s cases.)

Check for correct guesses made by the user and act accordinngly.

- **If** the guess is not a single alphabetic character:
    - Print an error message and continue.
- **If** the guess is already in guessed_letters:
    - Print a message that the letter has already been guessed and continue.
- Add the guess to guessed_letters.
- **If** all letters in the word are guessed:
    - Print a congratulations message and break the loop.
- **If** the guess is in the word:
    - Print a success message.
- **Else:**
    - Print a failure message.
    - Decrement attempts by 1.
- **If** attempts reach 0:
    - Print a game-over message and reveal the word.
- **Start the game** by calling hangman().
