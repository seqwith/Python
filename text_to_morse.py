#
# Michael Winder
# SEC 290 Summer B2
# Programming Assignment 3
# step_3.py
# July 25, 2020
#

def text_to_morse(letter):
    msg = ''
    if msg != ' ':
        msg += CODE[letter]
    else:
        msg = 'Unknown'
    return msg

CODE = {'a': '.--', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
        'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
        'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
        'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
        'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
        'z': '--..'
        }



letter = ''

while letter != '0':
    letter = input("Enter a letter (enter 0 to exit): ").lower()
    if letter == '0':
        print("Good Bye")
    else:
        encode = text_to_morse(letter)
        print("{} in Morse Code is {}" .format(letter, encode))
