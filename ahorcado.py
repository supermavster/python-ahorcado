# -*- coding: utf-8 -*-
# Library
import random

# Global Variables
ANSWERS = ['arroz', 'amarillo', 'amor', 'altar', 'ave', 'antro', 'azul', 'atomico',
           'beso', 'baston', 'brea', 'britanico', 'becerro', 'bote', 'blanco',
           'brasalete', 'brazo', 'bar', 'casa', 'centavo', 'cianuro', 'coco',
           'cuerpo', 'calabaza', 'cerro', 'cinturon', 'col', 'cruz', 'dado',
           'dragon', 'dos', 'diente', 'doctor', 'doce', 'duende', 'dardo', 'desde',
           'donde', 'efe', 'eres', 'elefante', 'entero', 'feo', 'frente', 'fase',
           'futbol', 'frase', 'frio', 'gato', 'gas', 'gel', 'gol', 'hola', 'hielo',
           'haz', 'iglesia', 'juez', 'londres']
CHALLENGE = ANSWERS[random.randint(0, len(ANSWERS) - 1)]


def run():
    letters = list(CHALLENGE)
    hiddenWord = ''
    lettersChalleng = []
    for letter in letters:
        lettersChalleng.append(" -*- ")
    showIntroduction()
    tries = -1
    while tries != 7:
        word = input('Write a word: ')
        response = checkAnswere(word)
        if response is False:
            tries += 1
        else:
            count = 0
            for letter in letters:
                if(word == letter):
                    lettersChalleng[count] = letter
                count += 1
            hiddenWord = '|'.join(lettersChalleng)
        if ''.join(lettersChalleng) != CHALLENGE:
            printBoy(tries)
            print(hiddenWord)
        else:
            congratulation()
            tries = 8
            break


def showIntroduction():
    print("   ▄████████    ▄█    █▄     ▄██████▄     ▄████████  ▄████████    ▄████████ ████████▄   ▄██████▄")
    print("  ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███ ███   ▀███ ███    ███")
    print("  ███    ███   ███    ███   ███    ███   ███    ███ ███    █▀    ███    ███ ███    ███ ███    ███")
    print("  ███    ███  ▄███▄▄▄▄███▄▄ ███    ███  ▄███▄▄▄▄██▀ ███          ███    ███ ███    ███ ███    ███")
    print("▀███████████ ▀▀███▀▀▀▀███▀  ███    ███ ▀▀███████▀   ███        ▀███████████ ███    ███ ███    ███")
    print("  ███    ███   ███    ███   ███    ███ ▀███████████ ███    █▄    ███    ███ ███    ███ ███    ███")
    print("  ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███ ███   ▄███ ███    ███")
    print("  ███    █▀    ███    █▀     ▀██████▀    ███    ███ ████████▀    ███    █▀  ████████▀   ▀██████▀")
    printBoy(-1)


def congratulation():
    print("███████╗███████╗██╗     ██╗ ██████╗██╗██████╗  █████╗ ██████╗ ███████╗███████╗")
    print("██╔════╝██╔════╝██║     ██║██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝")
    print("█████╗  █████╗  ██║     ██║██║     ██║██║  ██║███████║██║  ██║█████╗  ███████╗")
    print("██╔══╝  ██╔══╝  ██║     ██║██║     ██║██║  ██║██╔══██║██║  ██║██╔══╝  ╚════██║")
    print("██║     ███████╗███████╗██║╚██████╗██║██████╔╝██║  ██║██████╔╝███████╗███████║")
    print("╚═╝     ╚══════╝╚══════╝╚═╝ ╚═════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝")
    print("¡ Tu palabra es: {} !".format(CHALLENGE))
    exit()


def printBoy(position):
    man = [
        '0',
        '/', '|', '\\',
             '|',
        '/', '\\'
    ]
    sections = [
        '\n\t+--------+\n\t|\t |\n',
        '\n=========\n'
    ]
    body = ''
    for i in range(len(man)):
        if i <= position and position >= 0:
            if i == 0:
                body = '\t|\t ' + man[i]
            elif i > 0 and i < 4:
                if i == 1:
                    body = body + "\n\t|\t"
                body = body + man[i]
            elif i == 4:
                body = body + '|\t ' + man[i] + '\n\t|\t'
            elif i > 4:
                body = body + man[i] + " "

            if i > 2 and i < 4:
                body = body + '\n\t'
        else:
            if i > 0:
                body += "\n"
            body = body + '\t|\t'
    body = sections[0] + body + sections[1]
    print(body)


def printHiddenWord():
    print(['-' * len(CHALLENGE)])


def checkAnswere(word):
    letters = list(CHALLENGE)
    for letter in letters:
        if(word == letter):
            return True
    return False


if __name__ == "__main__":
    run()
