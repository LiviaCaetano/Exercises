num1 = (input('Digite o primeiro número: '))
num2 = (input('Digite o segundo número: '))
num3 = (input('Digite o terceiro número: '))
num1_int = int(num1)
num2_int = int(num2)
num3_int = int(num3)

menor = num1_int

if num2_int < menor:
    menor = num2_int

    if num3_int < menor:
        menor = num3_int

print (f'O menor número é: {menor}')