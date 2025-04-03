# Exercício 6
# Uma impressora trabalha com um sistema de fila para processar documentos
# enviados para impressão. Cada documento enviado entra no final da fila e será
# impresso na ordem em que chegou.
# • Crie uma fila vazia para representar a fila de impressão.
# • Enfileire três documentos (nomes de arquivos) na fila.
# • Mostre qual documento será impresso primeiro.
# • Desenfileire o primeiro documento e mostre o próximo da fila.
# • Verifique se ainda há documentos na fila após as remoções.

from collections import deque
import time


fila = deque()

fila.append("texto.txt")
fila.append("imagem.jpg")
fila.append("planilha.xlsx")

print(f"Arquivo que será impresso: {fila[0]}")
for i in range(5, 0, -1): 
        print(f"Imprimindo... {i} segundos restantes", end='\r')
        time.sleep(1)

fila.popleft()

print(f"Arquivo que será impresso: {fila[0]}")
for i in range(7, 0, -1):  
        print(f"Imprimindo... {i} segundos restantes", end='\r')
        time.sleep(1)

fila.popleft()

print(f"Arquivo que será impresso: {fila[0]}")
for i in range(9, 0, -1):  
        print(f"Imprimindo... {i} segundos restantes", end='\r')
        time.sleep(1)

fila.popleft()

if len(fila) == 0:
    print("Todos os documentos foram impressos.")
else:
    print("Ainda há documentos a serem impressos.")
 