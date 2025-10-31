contador = 1

while contador <= 100:
    num = contador
    divisores = 0
    i = 1

    # conta quantos divisores o número tem
    while i <= num:
        if num % i == 0:
            divisores += 1
        i += 1

    if divisores == 2:
        print(f'{num} é primo')

    contador += 1
