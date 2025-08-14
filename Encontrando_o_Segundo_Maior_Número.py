numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def segundo_maior(numeros):
    unicos = set(numeros)
    if len(unicos) < 2:
        return None
    return sorted(unicos)[-2]
print("O segundo maior numero é:", segundo_maior(numeros))

#{solução concluída do {Encontrando o Segundo Maior Número}}