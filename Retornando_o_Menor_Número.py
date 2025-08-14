numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def menor_numero(lista):
    if not lista:  # verifica se a lista está vazia
        return None
    menor = lista[0]
    for numero in lista:
        if numero < menor:
            menor = numero
    return menor

print("O menor número é:", (menor_numero(numeros)))

#{solução concluída do {Retornando o Menor Número}}