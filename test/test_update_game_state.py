import copy
import os
import sys

# Ensure project root is on sys.path so tests can import `main` when run from pytest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from main import update_game_state


def test_correct_guess_no_life_loss():
	secret = "apple"
	guesses = ["a"]
	updated, lives = update_game_state(secret, guesses, "p", 5)
	assert "p" in updated
	assert lives == 5
	assert guesses == ["a"]  # original unchanged


def test_incorrect_guess_decrements_life():
	secret = "apple"
	guesses = []
	updated, lives = update_game_state(secret, guesses, "z", 3)
	assert "z" in updated
	assert lives == 2


def test_case_insensitivity():
	secret = "Apple"
	guesses = []
	updated_upper, lives1 = update_game_state(secret, guesses, "P", 4)
	updated_lower, lives2 = update_game_state(secret, guesses, "p", 4)
	assert updated_upper == updated_lower
	assert lives1 == lives2 == 4


def test_invalid_inputs_no_change():
	secret = "apple"
	base = ["a"]
	for bad in ("", "1", "ab", "@"):
		updated, lives = update_game_state(secret, base, bad, 5)
		assert updated == base
		assert lives == 5
		assert updated is not base  # copy returned


def test_repeated_guess_is_noop_and_returns_copy():
	secret = "apple"
	base = ["a"]
	updated, lives = update_game_state(secret, base, "a", 5)
	assert updated == base
	assert updated is not base
	assert lives == 5


def test_immutability_original_list_not_mutated():
	secret = "banana"
	original = ["b"]
	original_copy = copy.deepcopy(original)
	updated, lives = update_game_state(secret, original, "n", 6)
	assert original == original_copy  # original list unchanged
	assert "n" in updated

import random
from main import update_game_state, build_masked_word, is_win

def test_update_game_state_correct_guess():
    word = "apple"
    guesses = ["a"]
    updated, lives = update_game_state(word, guesses, "p", 5)
    assert "p" in updated
    assert lives == 5

def test_update_game_state_incorrect_guess():
    word = "apple"
    guesses = []
    updated, lives = update_game_state(word, guesses, "z", 3)
    assert "z" in updated
    assert lives == 2

def test_update_game_state_invalid_input():
    word = "apple"
    guesses = ["a"]
    updated, lives = update_game_state(word, guesses, "", 5)
    assert updated == guesses
    assert lives == 5

def test_build_masked_word():
    word = "apple"
    guesses = ["a", "p"]
    masked = build_masked_word(word, guesses)
    assert masked == "a p p _ _"

def test_is_win_true():
    word = "apple"
    guesses = ["a", "p", "l", "e"]
    assert is_win(word, guesses)

def test_is_win_false():
    word = "apple"
    guesses = ["a", "p"]
    assert not is_win(word, guesses)