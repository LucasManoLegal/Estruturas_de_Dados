# 1) Crie uma função que receba duas listas de números inteiros e retorne uma nova lista contendo os elementos que aparecem em ambas as listas (interseção).

def intersecao_listas(lista1, lista2):
    intersecao = []
    for elemento in lista1:
        if elemento in lista2:
            intersecao.append(elemento)
    print(intersecao)

intersecao_listas([1, 2, 3], [4, 3, 6])

