# 4) Crie uma função que receba duas listas de números inteiros e retorne um conjunto com os números que aparecem em 
# ambas as listas.

def interseccao_listas(lista1, lista2):

    return set(lista1) & set(lista2)

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]

resultado = interseccao_listas(lista1, lista2)

print(resultado)
