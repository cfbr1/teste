def par_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

valor = int(input("Digite um número: "))
resultado = par_impar(valor)
print(f"O número {valor} é {resultado}.")