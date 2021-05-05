import pandas as pd
import random


def read_words(filename="palavras.txt"):

    with open(filename, 'r', encoding="utf8") as f:
        words = f.readlines()

    words = [x.strip("\n") for x in words]

    df = pd.DataFrame(columns={"words"})
    df["words"] = words
    df["n_letters"] = df["words"].apply(lambda x: len(x))

    return df


def get_word(df, letras):

    filtered = df[df["n_letters"] == letras]
    if len(filtered) == 0:
        raise ValueError("Nenhuma palavra com esse tamanho")

    return filtered.sample(n=1).iloc[0]


def display(word, show, lives):

    print(forca[lives])

    for pos, letter in enumerate(word):
        if show[pos]:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print()


def refresh_word_right(word, show, guess, lives):
    guessed_right = False

    for pos, letter in enumerate(word):
        if letter == guess:
            show[pos] = 1
            guessed_right = True

    if not guessed_right:
        lives = lives - 1

    return show, lives


def get_letter(letters_guessed):

    letter = input("Letra: ").lower()
    while letter in letters_guessed:
        letter = input("Tente outra letra: ").lower()

    letters_guessed.add(letter)

    return letter, letters_guessed


def menu(erro):
    print("Jogo da Forca".center(30), end="\n\n")
    print("1. Jogar")
    print("2. Sair")
    print()

    if erro:
        print("Erro: Digite 1 ou 2")
        opt = int(input("Opção: "))

    else:
        opt = int(input("Opção: "))

    return opt


def get_lives(n_letters):

    if n_letters < 5:
        return 6

    elif n_letters < 8:
        return 5

    else:
        return 4


def play():

    words = read_words()
    word, n_letters = get_word(words, random.randint(3, 10))
    letters_guessed = set()
    show = [0] * n_letters
    lives = get_lives(n_letters)
    win = False

    while lives > 0 and not win:
        display(word, show, lives)
        guess, letters_guessed = get_letter(letters_guessed)
        show, lives = refresh_word_right(word, show, guess, lives)
        if sum(show) == n_letters:
            win = True

    display(word, show, lives)

    if win:
        print("Parabéns! Você venceu!")
        input()

    else:
        print("Que pena, quem sabe da próxima vez...")
        input()


def main():

    erro = False
    while True:
        opt = menu(erro)
        erro = False
        if opt == 1:
            play()
        elif opt == 2:
            break
        else:
            erro = True


###########################################

forca = dict()
forca[0] =\
    """
_________
|       |
|       O
|      \\|/
|       |
|      /\\
|
|
"""

forca[1] =\
    """
_________
|       |
|       O
|      \\|/
|       |
|      /
|
|
"""

forca[2] =\
    """
_________
|       |
|       O
|      \\|/
|       |
|      
|
|
"""

forca[3] =\
    """
_________
|       |
|       O
|      \\|
|       |
|      
|
|
"""

forca[4] =\
    """
_________
|       |
|       O
|       |
|       |
|      
|
|
"""

forca[5] =\
    """
_________
|       |
|       O
|       
|       
|      
|
|
"""

forca[6] =\
    """
_________
|       |
|       
|       
|       
|      
|
|
"""
###########################################


if __name__ == "__main__":
    main()
