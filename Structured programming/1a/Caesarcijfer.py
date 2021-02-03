#TODO: Het programma is niet af en ik weet niet hoe ik het af moet maken, ik heb wel een versie online gevonden, maar vind dat ik dit soort dingen zelf moet kunnen oplossen.
# mijn eerste gedachten was om het Cyclisch verschuif algoritme te gebruiken. Maar heb het niet goed kunnen implementeren.
# Bottomline het is niet af.
# link: tutorialspoint.com/cryptography_with_python/cryptography_with_python_caesar_cipher.htm
import string

#To be or not to be, That is the question

def encrypt(s, r):

    alphabet_string = string.ascii_lowercase
    caesar_alphabet = alphabet_string
    for l in range(abs(r)):
        if r < 0:
            s = alphabet_string[-1] + alphabet_string
            s = alphabet_string[:-1]
        elif r > 0:
            s = alphabet_string + alphabet_string[0]
            s = alphabet_string[1:]

    return s



while True:

    tekst = input("Geef een tekst: ")
    rotation = int(input("Geef een rotatie: "))
    print(f"Caesarcode: {encrypt(tekst, rotation)}")


