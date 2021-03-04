#!/usr/bin/python3
import os
from random import choice
import The_hanged_man_scheme

slovo = choice(["obesenec", "auto", "autobus", "pondeli"])
tajenka = len(slovo) * ["_"]
zivoty = 7
hra_probiha = True
while hra_probiha and zivoty > 0:
    os.system("cls")
    print(The_hanged_man_scheme.hangman[7 - zivoty])
    print(f"Tajenka: {tajenka}, {zivoty}")
    hadani = input("Zadej pismeno nebo slovo: ").lower()
    if slovo == hadani:
        hra_probiha = False
    elif len(hadani) == 1 and hadani in slovo:
        for index, pismeno in enumerate(slovo):
            if pismeno == hadani:
                tajenka[index] = pismeno
        hra_probiha = False if "_" not in tajenka else True
    else:
        zivoty -= 1
if not hra_probiha:
    print("Uhod jsi slovo!")
else:
    os.system("cls")
    print(The_hanged_man_scheme.hangman[7 - zivoty])
    print(f"PROHRAL JSI, TAJNE SLOVO BYLO *{slovo}*")