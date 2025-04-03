# Exercício 5
# Um consultório odontológico precisa gerenciar a ordem de atendimento dos
# pacientes. Para isso, foi decidido implementar uma fila onde os pacientes são
# chamados na ordem em que chegaram (FIFO – First In, First Out).

from collections import deque

# Função que exibe o menu
def menu():
    print("-" * 20)
    print("O que deseja fazer?")
    print("-" * 20)
    print(" 1 - Cadastrar senha\n 2 - Chamar paciente\n 3 - Sair")
    print("-" * 20)

# Função para cadastrar a senha do paciente
def cadastrar_senha(contador, fila):
    contador += 1
    fila.append(contador)
    print(f"Senha {contador} cadastrada.")
    print(f"Fila atual: {fila}")
    return contador  # Retorna o contador atualizado

# Função para chamar o próximo paciente
def chamar_paciente(fila):
    if fila:
        paciente = fila.popleft()  # Remove o primeiro paciente da fila
        print(f"Paciente com senha {paciente} chamado.")
    else:
        print("Não há pacientes na fila.")

# Função principal que gerencia as opções
def opcao():
    fila = deque()  # Inicializa a fila
    contador = 0  # Inicializa o contador de senhas
    while True:
        menu()  # Exibe o menu
        try:
            acao = int(input("Escolha uma opção: "))  # Recebe a opção do usuário
        except ValueError:
            print("Opção inválida. Digite um número.")
            continue
        
        if acao == 1:  # Cadastrar senha
            contador = cadastrar_senha(contador, fila)  # Atualiza o contador
        elif acao == 2:  # Chamar paciente
            chamar_paciente(fila)
        elif acao == 3:  # Sair
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Chama a função principal
opcao()


    

