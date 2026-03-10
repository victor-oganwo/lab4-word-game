def update_game_state(
    secret_word: str, guessed_letters: list[str], guess: str, lives: int
) -> tuple[list[str], int]:
    """
    Updates game state based on player guess.

    Args:
        secret_word: The word to guess (normalized to lowercase internally)
        guessed_letters: List of previously guessed letters (treated as immutable)
        guess: Single letter guess (case-insensitive)
        lives: Remaining attempts

    Returns:
        Tuple of (updated_guessed_letters, updated_lives)

    Behavior:
        - Validates guess is a single alphabetic character; ignores invalid input
        - Treats repeated guesses as no-ops (no penalty, no update)
        - Decrements lives only on incorrect guesses
        - Returns new list to maintain input immutability
    """
    secret_word = secret_word.lower()
    guess = guess.lower()

    # Reject invalid guesses (empty, non-alphabetic, or multi-character)
    if not guess or len(guess) != 1 or not guess.isalpha():
        return guessed_letters[:], lives

    # Ignore repeated guesses
    if guess in guessed_letters:
        return guessed_letters[:], lives

    new_guessed_letters = guessed_letters + [guess]

    # Correct guess preserves lives; incorrect guess decrements
    if guess in secret_word:
        return new_guessed_letters, lives

    return new_guessed_letters, lives - 1


def build_masked_word(secret_word: str, guessed_letters: list[str]) -> str:
    """
    Build a masked display of the secret word, revealing guessed letters
    and using '_' for unrevealed letters.
    """
    guessed_set = {g.lower() for g in guessed_letters}
    result = []

    for char in secret_word:
        if char.isalpha():
            if char.lower() in guessed_set:
                result.append(char)
            else:
                result.append("_")
        else:
            result.append(char)

    return " ".join(result)


def is_win(secret_word: str, guessed_letters: list[str]) -> bool:
    """
    Check if the player has guessed all alphabetic letters in the secret word.
    """
    guessed_set = {g.lower() for g in guessed_letters}
    return all(char.lower() in guessed_set for char in secret_word if char.isalpha())


def play_round(
    secret_word: str, guessed_letters: list[str], lives: int, guess: str
) -> tuple[list[str], int, str, bool, bool]:
    """
    Process one round of the game: update state with the guess, build masked word, and check win/loss.
    Returns (new_guessed_letters, new_lives, masked_word, is_win, is_loss).
    """
    new_guessed_letters, new_lives = update_game_state(
        secret_word, guessed_letters, guess, lives
    )
    masked = build_masked_word(secret_word, new_guessed_letters)
    win = is_win(secret_word, new_guessed_letters)
    loss = new_lives <= 0
    return new_guessed_letters, new_lives, masked, win, loss


def play_one_game(
    secret_word: str,
    lives: int,
    input_fn=input,
    output_fn=print,
) -> bool:
    """
    Play one game loop with I/O separated. Returns True on win, False on loss.
    - No `while True`.
    - Keeps replay handling to caller.
    """
    guessed_letters: list[str] = []
    won = is_win(secret_word, guessed_letters)

    while lives > 0 and not won:
        output_fn(
            f"Word: {build_masked_word(secret_word, guessed_letters)}    Lives: {lives}"
        )
        guess = input_fn("Enter a letter: ").strip()
        guessed_letters, lives = update_game_state(
            secret_word, guessed_letters, guess, lives
        )
        won = is_win(secret_word, guessed_letters)

    if won:
        output_fn(f"You won! Word: {secret_word}")
        return True

    output_fn(f"You lost. Word was: {secret_word}")
    return False


import random


def main(input_fn=input, output_fn=print) -> None:
    """
    Minimal entry point: selects a random word, runs one game, supports replay.
    Keeps I/O via input_fn/output_fn to separate UI from logic.
    """
    words = ["apple", "banana", "cherry", "python", "hangman"]
    lives = 6

    play_again = True
    while play_again:
        secret = random.choice(words)
        play_one_game(secret, lives, input_fn=input_fn, output_fn=output_fn)
        resp = input_fn("Play again? [y/N]: ").strip().lower()
        play_again = resp.startswith("y")


def main(input_fn=input, output_fn=print) -> None:
    """
    Minimal entry point: selects a random word, runs one game, supports replay.
    Now supports easy, medium, and hard difficulty levels.
    """
    words = ["apple", "banana", "cherry", "python", "hangman"]
    difficulty_lives = {"easy": 8, "medium": 6, "hard": 4}

    play_again = True
    while play_again:
        resp = input_fn("Choose difficulty [easy/medium/hard]: ").strip().lower()
        lives = difficulty_lives.get(resp, 6)

        secret = random.choice(words)
        play_one_game(secret, lives, input_fn=input_fn, output_fn=output_fn)

        replay = input_fn("Play again? [y/N]: ").strip().lower()
        play_again = replay.startswith("y")


if __name__ == "__main__":
    main()
