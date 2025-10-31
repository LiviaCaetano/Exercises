import math

valor_a = (input('Digite um valor para A: '))
valor_b = (input('Digite um valor para B: '))
valor_c = (input('Digite um valor para C: '))
a_int = int(valor_a)
b_int = int(valor_b)
c_int = int(valor_c)

soma = b_int + c_int

triangulo = soma > a_int

if (triangulo):
    print ('Os valores formam um triângulo')

    p = (a_int + b_int + c_int) / 2  
    area = math.sqrt(p * (p - a_int) * (p - b_int) * (p - c_int))

    print (f'A área é desse triângulo é: {area}')
else:
    print (f'Os valores {a_int}, {b_int} e {c_int} não formam um triângulo')