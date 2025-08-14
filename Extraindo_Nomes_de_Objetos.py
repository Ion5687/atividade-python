lista = [
    {"nome": "Thiago"},
    {"nome": "Carla"},
    {"nome": "Matheus"},
    {"nome": "Felipe"}
]

def retorna_nome(lista):
    nomes = []
    for item in lista:
        nomes.append(item["nome"])
    return nomes
print(retorna_nome(lista))

#{solução concluída do {Extraindo Nomes de Objetos}}