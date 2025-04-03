# Exercício 7
# Uma central de atendimento telefônico gerencia chamadas em espera usando
# uma pilha. Isso significa que a última chamada recebida será a primeira a ser
# atendida.
# • Crie uma pilha vazia para armazenar as chamadas em espera.
# • Empilhe três chamadas com identificadores numéricos.
# • Mostre qual chamada será atendida primeiro.
# • Atenda a última chamada recebida e mostre a nova chamada no topo da
# pilha.
# • Verifique se ainda há chamadas na pilha após os atendimentos.

pilha_de_chamadas = []


pilha_de_chamadas.append(101)  
pilha_de_chamadas.append(102)  
pilha_de_chamadas.append(103)  

chamada_atendida_primeiro = pilha_de_chamadas[-1]
print(f"A chamada que será atendida primeiro é a de identificador: {chamada_atendida_primeiro}")


chamada_atendida = pilha_de_chamadas.pop()
print(f"Chamada atendida: {chamada_atendida}")

if pilha_de_chamadas:
    nova_chamada_topo = pilha_de_chamadas[-1]
    print(f"A nova chamada no topo da pilha é a de identificador: {nova_chamada_topo}")
else:
    print("Não há mais chamadas na pilha.")

if pilha_de_chamadas:
    print(f"Ainda há chamadas na pilha. Total de chamadas: {len(pilha_de_chamadas)}")
else:
    print("A pilha está vazia.")
