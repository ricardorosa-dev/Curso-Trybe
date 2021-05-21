NOTES = ["Marcos 10\n", "Felipe 4\n", "José 6\n", "Ana 10\n", "Maria 9\n", "Miguel 5"]

file = open("notes.txt", mode="w+")
file.writelines(NOTES)

lines = file.readlines()
print(lines)

file.close()

# TEM QUE FECHAR APOS CADA OPERAÇÃO? SENÃO NÃO CONSEGUE VER AS MUDANÇAS??
