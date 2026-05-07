print('---CIFRA DE CESAR---\n')

alfabeto_min = 'abcdefghijklmnopqrstuvwxyz'
alfabeto_mai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
valor = list(range(1, 27))

alfa_min = list(alfabeto_min)
alfa_mai = list(alfabeto_mai)

letrasmin_valor = dict(zip(alfa_min, valor))  # dict(zip()) junta duas listas
# print(letras_valor) #  {'a': 1, 'b': 2, ...}
letrasmai_valor = dict(zip(alfa_mai, valor))

letra_valor = []
letra_valor_novo = []
string_nova = []

string = input('digite a string: ').strip()
# strings = (string.replace(' ','')) [solução que tentei dar
# para os espaços, porém não dá muito certo porque mexe na estrutura toda
chave = int(input('digite a chave: '))

for letra in string:
    if letra in letrasmin_valor:
        letra_valor.append(letrasmin_valor[letra])
    elif letra in letrasmai_valor:
        letra_valor.append(letrasmai_valor[letra])
    else:
        letra_valor.append(letra)

for num in letra_valor:
    if type(num) != int:
        letra_valor_novo.append(num)
        continue
    valor_novo = (num + chave) % 26
    if valor_novo == 0:
        valor_novo = 26
    letra_valor_novo.append(valor_novo)

# print(letra_valor)
# print(letra_valor_novo)

valor_letrasmin = dict(zip(valor, alfa_min))
# print(valor_letras)  # {'1': a, '2': b, ...}
valor_letrasmai = dict(zip(valor, alfa_mai))

for i, num in enumerate(letra_valor_novo):
    if type(num) != int:
        string_nova.append(num)
    elif string[i].isupper():
        string_nova.append(valor_letrasmai[num])
    else:
        string_nova.append(valor_letrasmin[num])

# print(string_nova)
print(f"String: {''.join(string_nova)}")
print(f'Chave: {chave}')


