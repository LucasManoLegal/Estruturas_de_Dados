# Tipos de Dados Abstratos em Python

Tipos de dados abstratos (TDA) são modelos de estrutura de dados que definem operações possíveis, independentemente de sua implementação. Dois TDAs comuns são **pilhas** e **filas**.

## 1. Pilhas (Stacks)

Uma pilha segue o princípio **LIFO** (Last In, First Out - último a entrar, primeiro a sair). A inserção e remoção de elementos ocorrem no topo da pilha.

### Exemplo com lista:
```python
pilha = []

# Adicionando elementos (push)
pilha.append(1)
pilha.append(2)
pilha.append(3)

# Removendo elementos (pop)
print(pilha.pop())  # Saída: 3
print(pilha.pop())  # Saída: 2
```

## 2. Filas (Queues)

Uma fila segue o princípio **FIFO** (First In, First Out - primeiro a entrar, primeiro a sair). Os elementos são adicionados no final da fila e removidos do início.

### Exemplo com `collections.deque`:
```python
from collections import deque

fila = deque()

# Adicionando elementos (enqueue)
fila.append("A")
fila.append("B")
fila.append("C")

# Removendo elementos (dequeue)
print(fila.popleft())  # Saída: A
print(fila.popleft())  # Saída: B
```

## Quando usar?

- **Pilhas**: úteis para algoritmos de recursão, desfazer/refazer, avaliação de expressões matemáticas.
- **Filas**: boas para sistemas de atendimento, agendamento de tarefas, gerenciamento de processos.

## Conclusão

Apesar de listas em Python poderem ser usadas para simular pilhas e filas, usar estruturas como `deque` é mais eficiente em operações de inserção e remoção em ambos os extremos.
