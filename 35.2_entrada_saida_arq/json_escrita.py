import json

with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

# ACESSAR UMA CHAVE
# print(pokemons[0]["evolution"])

grass_type_pokemons = [
    pokemon for pokemon in pokemons if "Grass" in pokemon["type"]
]

with open("grass_pokemons.json", "w") as file:
    # json.dumps joga numa variavel
    # json_to_write = json.dumps(grass_type_pokemons) #converte de python pra json
    # file.write(json_to_write)
    
    # json.dump joga direto no arquivo
    json.dump(grass_type_pokemons, file)
