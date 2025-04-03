# 2) Crie uma função que receba uma lista de tuplas, onde cada tupla contém o nome de um aluno e sua nota, e retorne o nome do aluno com a maior nota.

def aluno_maior_nota(lista_alunos):
    lista_notas = []
    for aluno in lista_alunos:
        lista_notas.append(aluno[1])
    maior_nota = max(lista_notas)
    for aluno in lista_alunos:
        if aluno[1] == maior_nota:
            melhor_aluno = aluno[0]
            print(f"Aluno com maior nota: {melhor_aluno} | Nota: {maior_nota}")
            break
    
aluno_maior_nota([("Lucas", 10), ("Beatriz", 2), ("Gabriel", 7)])
        
    



