nome = input("Escreva seu nome: ")
# print(nome.upper())

# de cima pra baixo
write_name = []

for letter in range(len(nome)):
    write_name.append(nome[letter])
    my_string = ''.join(write_name)
    print(my_string.upper())
    
#de baixo pra cima
new_name = nome

for letter in range(len(nome)):
    print(new_name.upper())
    new_name = new_name[:-1]
