print('---CIFRA DE CESAR---\n')

def cifrar(string, chave):
    alfabeto_min = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_mai = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    valor = list(range(1, 27))

    letrasmin_valor = dict(zip(list(alfabeto_min), valor))
    letrasmai_valor = dict(zip(list(alfabeto_mai), valor))
    valor_letrasmin = dict(zip(valor, list(alfabeto_min)))
    valor_letrasmai = dict(zip(valor, list(alfabeto_mai)))


    resultado = []
    for i, letra in enumerate(string):
        if letra in letrasmin_valor:
            novo = letrasmin_valor[letra] + chave
            resultado.append(valor_letrasmin[novo % 26 or 26])
#  substitui o if valor_novo == 0
        elif letra in letrasmai_valor:
            novo = letrasmai_valor[letra] + chave
            resultado.append(valor_letrasmin[novo % 26 or 26])
        else:
            resultado.append(letra)

    return ''.join(resultado)

string = input('digite a string: ').strip()
chave = int(input('digite a chave: '))

print(f'String: {cifrar(string, chave)}')
print(f'Chave: {chave}')




