def palindromo(palavra):
    palavra_invertida = palavra[::-1]
    if palavra == palavra_invertida:
        return True
    else:
        return False

texto = input("Digite uma palavra: ")
if palindromo(texto):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")