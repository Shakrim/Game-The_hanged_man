#!/usr/bin/python3
import os
from random import choice
import The_hanged_man_scheme

guessed_word = choice(["sex", "sibling", "cholesterol", "monday","lesbian"])
puzzle = len(guessed_word) * ["_"]
life = 7
game_on = True
while game_on and life > 0:
    os.system("cls")
    print(The_hanged_man_scheme.hangman[7 - life])
    print(f"Puzzle: {puzzle}, {life}")
    guessing = input("Enter letter or guessed word: ").lower()
    if guessed_word == guessing:
        game_on = False
    elif len(guessing) == 1 and guessing in guessed_word:
        for index, letter in enumerate(guessed_word):
            if letter == guessing:
                puzzle[index] = letter
        game_on = False if "_" not in puzzle else True
    else:
        life -= 1
if not game_on:
    print("You got it!")
else:
    os.system("cls")
    print(The_hanged_man_scheme.hangman[7 - life])
    print(f"You failed, the quessed word was *{guessed_word}*")