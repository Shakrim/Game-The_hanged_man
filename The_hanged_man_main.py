#!/usr/bin/python3
import os
from random import choice
import The_hanged_man_scheme

def actual_game_Status(lives:int, puzzle:list, game_on:bool)->None:
    os.system("cls")
    status = f"Puzzle: {' '.join(puzzle)} Lives left: {lives}"
    print(status, The_hanged_man_scheme.hangman[7 - lives], sep="\n")
    if not game_on and lives:
        print("You won!")

    elif not lives:
        print("You lost!")

guessed_word = choice(["sex", "sibling", "cholesterol", "monday","lesbian"])
puzzle = len(guessed_word) * ["_"]
lives = 7
game_on = True



while game_on and lives > 0:
    actual_game_Status(lives, puzzle, game_on)
    guessing = input("Enter letter or guessed word: ").lower()

    if guessed_word == guessing:
        game_on = False
    elif len(guessing) == 1 and guessing in guessed_word:
        for index, letter in enumerate(guessed_word):
            if letter == guessing:
                puzzle[index] = letter
        game_on = False if "_" not in puzzle else True
    else:
        lives -= 1

actual_game_Status(lives, puzzle, game_on)




