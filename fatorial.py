def fatorial_recursivo(n: int) -> int:
    if n < 0:
        raise ValueError("Número não pode ser negativo.")

    if n == 0 or n == 1:
        return 1

    return n * fatorial_recursivo(n - 1)


def fatorial_iterativo(n: int) -> int:
    if n < 0:
        raise ValueError("Número não pode ser negativo.")

    resultado = 1
    for i in range(2, n + 1):
        resultado *= i

    return resultado


def menu():
    print("\n=== CALCULADORA DE FATORIAL ===")
    print("1 - Fatorial Recursivo")
    print("2 - Fatorial Iterativo")
    print("0 - Sair")


def main():
    while True:
        menu()

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Erro: escolha uma opção válida (número).")
            continue

        if opcao == 0:
            print("Encerrando o programa...")
            break

        if opcao not in [1, 2]:
            print("Opção inválida. Tente novamente.")
            continue

        try:
            numero = int(input("Digite um número inteiro não negativo: "))

            if numero < 0:
                print("Erro: número não pode ser negativo.")
                continue

        except ValueError:
            print("Erro: digite apenas números inteiros.")
            continue

        try:
            if opcao == 1:
                resultado = fatorial_recursivo(numero)
                print(f"Fatorial recursivo de {numero} = {resultado}")

            elif opcao == 2:
                resultado = fatorial_iterativo(numero)
                print(f"Fatorial iterativo de {numero} = {resultado}")

        except Exception:
            print("Ocorreu um erro inesperado.")


if __name__ == "__main__":
    main()