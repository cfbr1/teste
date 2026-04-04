valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))

print("Escolha a operação: 0 - Soma, 1 - Subtração, 2 - Multiplicação, 3 - Divisão")

opcao = int(input("Digite a opção: "))

if opcao == 0:
    soma = valor1 + valor2 
    print("A soma dos valores digitados é:", soma)

elif opcao == 1:
    subtracao = valor1 - valor2
    if valor1 < valor2:
       print("O resultado é negativo:", subtracao)
    else:
        print("O resultado da subtração é:", subtracao)

elif opcao == 2:
    multiplicacao = valor1 * valor2
    print("O resultado da multiplicação é:", multiplicacao)

elif opcao == 3:
    if valor2 != 0:
        divisao = valor1 / valor2
        print("O resultado da divisão é:", divisao)
    else:
        print("Erro: divisão por zero não é permitida.")

else:
    print("Opção inválida. Por favor, revise.")