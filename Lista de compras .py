lista_de_compras = ["Frango", "Arroz", "Feijão", "Pera", "Abacaxi"]
print(lista_de_compras)

lista_de_compras.insert(0, input("digite o Alimento: "))
print(lista_de_compras)

#lista_de_compras.append(input("Digite o alimento: "))
#print(lista_de_compras)

lista_de_compras.remove("Frango")
print(lista_de_compras)

lista_de_compras.pop()
print(lista_de_compras)

print(len(lista_de_compras))
print(lista_de_compras.count("Feijão"))

lista_de_compras.sort()
print(lista_de_compras)

lista_de_compras.reverse()
print(lista_de_compras)