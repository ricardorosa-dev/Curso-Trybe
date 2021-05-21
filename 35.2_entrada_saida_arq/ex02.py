import sys

numeros = input("Adicione numeros para serem somados, separados por um espaço\n")

num_array = numeros.split(" ")
soma = 0

for numero in num_array:
    if (not numero.isdigit()):
        err = f"Erro ao somar valores, {numero} é um valor inválido"
        print(f"{err}", file=sys.stderr)
        exit()

for num in num_array:
    soma += int(num)

print(soma)
