# My Original Thinking

## App States
- Start the game
- Playing it
- Win
- Lose

## App Variables
- secret word
- guessed letters
- remaining tries
- it shows the current word display
- the user inputs

## App Rules and Invariants
- Player guesses one letter at a time
- Correct letter is revealed
- Wrong letter reduces tries
- Same guess should not count twice
- Game ends when word is guessed or tries reach 0

## App Bugs
- Empty input
- More than one letter entered
- Number or symbol entered
- Repeated guess
- Uppercase/lowercase issue
# Copilot Suggestions

## App States
- Initialization / Start
- Playing / Waiting for input
- Correct guess
- Incorrect guess
- Win
- Lose
- Game over

## App Variables
- word_to_guess
- guessed_word / current display
- remaining_attempts
- max_attempts
- guessed_letters
- current_guess
- correct_guesses
- incorrect_guesses
- game_won
- game_lost

## App Rules and Invariants
- The word should be chosen at the start and hidden from the player
- The player guesses one letter at a time
- Guesses should be case-insensitive
- Only alphabetic input should be accepted
- Repeated guesses should not reduce attempts
- Correct guesses should reveal all matching positions in the word
- Incorrect guesses should reduce remaining attempts
- The game ends when the word is guessed or attempts reach zero
- guessed_word should always match the revealed letters so far
- remaining_attempts should never go below 0
- guessed_letters should not contain duplicates
- game_won and game_lost cannot both be true

## App Bugs
- Case sensitivity issues
- Repeated guesses counting more than once
- Invalid input like numbers or symbols
- Empty input
- guessed_word not updating correctly
- Repeated letters not all being revealed
- remaining_attempts going below 0
- Game continuing after win or loss
- Empty or invalid word list

## Observations
For states and variables, Copilot was helpful but slightly overcomplicated because it included optional ideas like pause, score, hints, and difficulty.
For rules and bugs, the extra detail was useful because it highlighted important edge cases and invariants that are easy to forget.
Overall, Copilot helped expand the design, but I still needed to select only the parts that fit a simple Hangman-style game.
 The game should handle an empty or invalid word list safely