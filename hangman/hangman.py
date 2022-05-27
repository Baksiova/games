slova = ["pes", "macka","dom","slovensko","kvety","kytky"]
import random
slovo = random.choice(slova)
HANGMANPICS = ['''
    +---+
    |   |
        |
        |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
        |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
    |   |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
   /|   |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
   /|\  |
        |
        |
   =========''','''
    +---+
    |   |
    o   |
   /|\  |
   /    |
        |
   ========''','''
    +---+
    |   |
    o   |
   /|\  |
   / \  |
        |
   ========''']

import re



def guess():
    tries=7
    tip = ("-"*len(slovo))
    while tries >0 or len(tip) <len(slovo):
        char = input("Hadaj pismeno ")

        if len(char)<=0:
            char = input("Musis zadat 1 pismeno  ")
        elif len(char) > 1:
            return f"Zadaj jen 1 pismeno"

        if char in slovo:
            index= slovo.index(char)
            temp = list(tip)
            indices = [char.start() for char in re.finditer(char, slovo)]
            for x in indices:
                temp[x] = char
            tip = "".join(temp)
            print(f"Aktualny stav: {tip}")

            if tip == slovo:
                return f"Gratulujem vyhral si, slovo bolo {slovo}"
                break

            print(HANGMANPICS[-int(tries)])
        else:
            tries=tries-1
            print(f"Aktualny stav: {tip}")
            print(f"Mas {tries} zivotov")
            print(HANGMANPICS[-int(tries)])
    if tries ==0:
        input_2 =input("prehral si, chces hrat znovu?")
        if input_2 == "ano":
            print(guess())


print(guess())