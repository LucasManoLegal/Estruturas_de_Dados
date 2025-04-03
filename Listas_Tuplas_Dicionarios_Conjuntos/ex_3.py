# 3) Crie um programa que simule um dicionário de contatos. O programa deve permitir adicionar novos contatos (nome e número de telefone), buscar o número de telefone
# de um contato pelo nome e listar todos os contatos.

contatos = [
    {"Nome": "João", "Número": 987654321},
    {"Nome": "Gabriela", "Número": 998765432},
    {"Nome": "Davi", "Número": 912345678},
    {"Nome": "Matheus", "Número": 934567890}
]

def adicionar_contato():
    nome_contato = input("Digite o nome do contato: ").strip()
    numero_contato = input("Digite o número do contato: ").strip()
    
    if not numero_contato.isdigit():
        print("Erro: O número deve conter apenas dígitos.")
        return
    
    contatos.append({"Nome": nome_contato, "Número": int(numero_contato)})
    print(f"Contato {nome_contato} adicionado com sucesso!")

def exibir_contatos():
    if not contatos:
        print("Nenhum contato salvo.")
        return

    print("Lista de Contatos:")
    print("-" * 25)
    for contato in contatos:
        print(f"Nome: {contato['Nome']} Número: {contato['Número']}")
        print("-" * 25)

def buscar_contato():
    nome_busca = input("Digite o nome do contato que deseja buscar: ").strip()
    for contato in contatos:
        if contato["Nome"] == nome_busca:
            print(f"Nome: {contato['Nome']} - Número: {contato['Número']}")
            return
    print("Contato não encontrado.")

def menu():
    while True:
        print("Menu:")
        print("1 - Ver contatos")
        print("2 - Adicionar contato")
        print("3 - Buscar contato")
        print("4 - Sair")
        
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == "1":
            exibir_contatos()
        elif escolha == "2":
            adicionar_contato()
        elif escolha == "3":
            buscar_contato()
        elif escolha == "4":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()

