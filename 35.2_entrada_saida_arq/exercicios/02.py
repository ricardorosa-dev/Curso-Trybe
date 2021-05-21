import random

WORDS = ["Mulher", "Biquini", "Comprar", "Mensagem", "Ambulância", "Puro", "Banco", "Harmonia", "Costurar", "Culpado"]

word = random.choice(WORDS)
scramble = "".join(random.sample(word, len(word))).lower()

for trials in range(3):
    guess = input(f"Find out the word: {scramble}\n")
    if (guess == word.lower()):
        print("Você acertou! A palavra era", word)
        exit()

print("Você não conseguiu :(")
