
dicionario = {
    "YODA": "MESTRE JEDI",
    " Mace Windu": "Mestre jedi",
   "Anajin Skywalker" : "Cavaleiro Jedi",
    "R2-D2":"Droide",
   "Dex" : "Balconista",
    "Jonathan" : "Lolzero"
}

for chave, valor in dicionario.items():
    print("{} - {}" .format(chave, valor))

dicionario.pop("YODA")

for chave, valor in dicionario.items():
    print("{} - {}" .format(chave, valor))

