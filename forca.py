import random

def print_hangman(errors):
    if errors == 0:
        print(" ____\n|    |\n|    \n|    \n|   \n|\n")
    elif errors == 1:
        print(" ____\n|    |\n|    O\n|    \n|   \n|\n")
    elif errors == 2:
        print(" ____\n|    |\n|    O\n|    |\n|   \n|\n")
    elif errors == 3:
        print(" ____\n|    |\n|    O\n|   /|\n|   \n|\n")
    elif errors == 4:
        print(" ____\n|    |\n|    O\n|   /|\\\n|   \n|\n")
    elif errors == 5:
        print(" ____\n|    |\n|    O\n|   /|\\\n|   / \n|\n")
    else:
        print(" ____\n|    |\n|    O\n|   /|\\\n|   / \\\n|\n")

def play(word, max_errors):
    word = word.upper()
    guessed_letters = set()
    correct_letters = set(word)
    errors = 0

    print("Adivinhe a palavra:")
    while True:
        print_hangman(errors)

        for letter in word:
            if letter in guessed_letters:
                print(letter, end=" ")
            else:
                print("_", end=" ")
        print("\n")

        if correct_letters.issubset(guessed_letters):
            print("Parabéns, você ganhou!")
            break
        elif errors >= max_errors:
            print("Game over! A palavra era:", word)
            break

        guess = input("Digite uma letra: ").upper()
        if guess in guessed_letters:
            print("Você já tentou essa letra. Tente novamente.\n")
        elif guess in correct_letters:
            guessed_letters.add(guess)
        else:
            errors += 1
            guessed_letters.add(guess)
            print("Letra errada.\n")

words = ["python", "java", "javascript", "ruby", "html", "css"]
max_errors = 6

print("Bem-vindo ao jogo da forca!")
word = random.choice(words)
play(word, max_errors)
