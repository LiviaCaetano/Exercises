def inverter(frase):
    palavra = ""
    frase_invertida = ""

    for letra in frase:
        if letra != " ":
            palavra += letra
        else:
            frase_invertida += palavra[::-1] + " "
            palavra = ""

    frase_invertida += palavra[::-1]

    return frase_invertidas

texto = input("Digite uma frase: ")
resultado = inverter(texto)
print("Frase com palavras invertidas:", resultado)
