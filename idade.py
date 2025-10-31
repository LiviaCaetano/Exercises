idade_dias = input ('Digite  a idade em dias: ')
idade_int = int(idade_dias)

anos = idade_int // 365
meses = idade_int // 30

print (f'Idade expressa em {anos} anos')
print (f'Idade expressa em {meses} meses')
print(f'Idade expressa em {idade_int} dias')