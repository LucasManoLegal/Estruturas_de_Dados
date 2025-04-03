# Exercício 4

# Criar uma implementação simples de uma fila (Queue) usando listas.

# 1. Crie uma fila vazia.
# 2. Enfileire 3 números inteiros na fila.
# 3. Mostre o primeiro elemento da fila.
# 4. Desenfileire o primeiro elemento e mostre o novo primeiro elemento.
# 5. Verifique se a fila está vazia após as remoções.

from collections import deque

fila = deque()

fila.append(3)
fila.append(6)
fila.append(9)

print(fila[0])

fila.popleft()

print(fila[0])

fila.popleft()
fila.popleft()

if len(fila) == 0:
    print("A fila está vazia.")
else:
    print("A fila não está vazia.")