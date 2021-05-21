import random

WORDS = []
with open("palavras.txt") as file:
    # WORDS = file.read()
    for line in file.readlines():
        new_line = line.strip("\n")
        WORDS.append(new_line)

print(WORDS)

word = random.choice(WORDS)
scramble = "".join(random.sample(word, len(word))).lower()

for trials in range(3):
    guess = input(f"Find out the word: {scramble}\n")
    # print(word)
    if (guess == word.lower()):
        print("Você acertou! A palavra era", word)
        exit()

print("Você não conseguiu :(")
