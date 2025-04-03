# Tipos de Dados em Python

Python possui diversos tipos de dados embutidos que ajudam na manipulação eficiente de coleções de elementos. Entre os mais comuns, temos:

## 1. Listas

As listas são coleções ordenadas e mutáveis. Elas permitem armazenar múltiplos itens em uma única variável e podem conter diferentes tipos de dados.

### Exemplo:
```python
# Criando uma lista
frutas = ["maçã", "banana", "laranja"]

# Acessando elementos
print(frutas[0])  # Saída: maçã

# Adicionando elementos
frutas.append("uva")

# Removendo elementos
frutas.remove("banana")

# Percorrendo uma lista
for fruta in frutas:
    print(fruta)
```

## 2. Tuplas

Tuplas são semelhantes às listas, porém imutáveis. Ou seja, após sua criação, seus elementos não podem ser modificados.

### Exemplo:
```python
# Criando uma tupla
cores = ("vermelho", "verde", "azul")

# Acessando elementos
print(cores[1])  # Saída: verde
```

## 3. Dicionários

Dicionários armazenam pares de chave-valor, permitindo um acesso eficiente aos dados.

### Exemplo:
```python
# Criando um dicionário
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

# Acessando valores
print(pessoa["nome"])  # Saída: João

# Adicionando novos pares chave-valor
pessoa["profissão"] = "Engenheiro"

# Removendo um item
pessoa.pop("idade")
```

## 4. Conjuntos

Conjuntos são coleções não ordenadas de elementos únicos.

### Exemplo:
```python
# Criando um conjunto
numeros = {1, 2, 3, 4, 5}

# Adicionando elementos
numeros.add(6)

# Removendo elementos
numeros.discard(3)

# Verificando a existência de um elemento
print(4 in numeros)  # Saída: True
```

## Conclusão

Cada tipo de dado tem sua finalidade e uso adequado. As listas são úteis quando precisamos de coleções ordenadas e mutáveis. Tuplas são boas para dados imutáveis. Dicionários são excelentes para armazenar associações chave-valor, e conjuntos são ideais para coleções de itens únicos sem ordem específica.
