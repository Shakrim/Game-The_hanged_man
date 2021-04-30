#!/usr/bin/python3
import os
from random import choice

from The_hanged_man_scheme import hangman
from List_of_guessed_words import list_of_words


def puzzle_generation() -> str:
    guessed_word = choice(list_of_words)
    puzzle = len(guessed_word) * ["_"]
    return guessed_word, puzzle


def actual_game_Status(lives:int, puzzle:list, game_on:bool) -> None:
    os.system("cls")
    status = f"Puzzle: {' '.join(puzzle)} Lives left: {lives}"
    print(status, hangman[7 - lives], sep="\n")
    if not game_on and lives:
        print("You won!")

    elif not lives:
        print("You lost!")

def letter_check(guessed_word, puzzle, guessing):
    for index, letter in enumerate(guessed_word):
        if letter == guessing:
            puzzle[index] = letter
    return False if "_" not in puzzle else True



lives = 7
game_on = True

guessed_word, puzzle = puzzle_generation()

while game_on and not lives:
    actual_game_Status(lives, puzzle, game_on)
    guessing = input("Enter letter or guessed word: ").lower()

    if guessed_word == guessing:
        game_on = False
    elif len(guessing) == 1 and guessing in guessed_word:
        game_on = letter_check(guessed_word, puzzle, guessing)
    else:
        lives -= 1

actual_game_Status(lives, puzzle, game_on)




