
import random
from Grafik import ebenen, ueberschrift
from wortliste import woerter

Spiel_vorbei = False

chosen_word = random.choice(woerter)
word_length = len(chosen_word)

leben = 6

display = []
for i in range(word_length):
    display.append("_")

    print(f"{ueberschrift}\n")

    print(f"{' '.join(display)}")

while not Spiel_vorbei:

    guess = input("\nWelcher Buchstabe könnte in diesem Wort enthalten sein?\n").lower()

    for position in range(word_length):
        letter = chosen_word[position]
    if  letter == guess:
        display[position] = letter

    if guess not in chosen_word:
        leben -= 1
        print(f"Du hast {guess} geraten, dieser Buchstabe ist nicht im Wort enthalten, du verlierst ein Leben.")
    if  leben == 0:
        Spiel_vorbei = True
        print("\nDu hast verloren.")
        print("\nDas gesuchte Wort wäre" , chosen_word , "gewesen. Tja, sollte nicht sein")

    print(ebenen[leben])

    print(f"{' '.join(display)}")

    if "_" not in display:
        Spiel_vorbei = True
        print("\nDu hast gewonnen ;)")
        print(chosen_word)