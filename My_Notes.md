# My Original Thinking

## Game States
Possible states of a word guessing game (like Hangman):

- Start state (game begins)
- Playing state (user is guessing letters)
- Correct guess state
- Incorrect guess state
- Win state (player guesses the whole word)
- Lose state (player runs out of attempts)

## Variables Required

- secret_word → the word the player must guess
- guessed_letters → letters the player already tried
- remaining_attempts → number of guesses left
- current_display → word with hidden letters (example: _ _ a _ _)
- game_over → boolean to know if the game ended
- player_guess → the letter the player enters

## Rules and Invariants

- Player guesses one letter at a time
- If the letter is in the word → reveal it
- If not → decrease remaining attempts
- Player wins if all letters are revealed
- Player loses if attempts reach zero
- Letters already guessed cannot be used again

## Possible Bugs / Edge Cases

- Player enters more than one letter
- Player enters numbers or symbols
- Player repeats the same guess
- Word contains repeated letters
- Case sensitivity (A vs a)
- Empty input from player

# Copilot Suggestions

## App States
(start, playing, win, lose)

## App Variables
secret_word
guessed_letters
remaining_attempts
current_display
player_guess