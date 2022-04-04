notas = []

opcao = -1
while opcao !=4:
    print("1 - Informar notas \n 2 - exibir notas \n 3 - Calcular média \n 4 - para sair")
    opcao = int(input("Escolha sua opção: "))
    if(opcao==1):
        notas.append(float(input("Digite a nota: ")))
    elif opcao==2:
        for x in notas:
            print(x)
    elif opcao==3:
        print(" A média é {}" .format(sum(notas)/ len(notas)))



