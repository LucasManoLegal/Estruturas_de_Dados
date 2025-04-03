# Exercício 3

# Você foi contratado para desenvolver uma funcionalidade de “Desfazer/Refazer"
# para um editor de texto simples. O editor permite que o usuário escreva palavras
# em um documento, e, caso cometa um erro, pode desfazer a última ação ou
# refazê-la caso mude de ideia.


pilha = []
pilha_refazer = []

def menu():
    while True:
        texto = input("Digite as palavras desejadas: (z para desfazer, y para refazer, f para finalizar)").lower()
        match texto:
            case "z": 
                if pilha:
                    palavra = pilha.pop()
                    pilha_refazer.append(palavra)
                    exibir_texto()
                else:
                    print("Não há mais nada para desfazer.")
            case "y":  
                if pilha_refazer:
                    palavra = pilha_refazer.pop()
                    pilha.append(palavra)
                    exibir_texto()
                else:
                    print("Não há mais nada para refazer.")
            case "f":
                print("Finalizando o programa.")
                break
            case _:  
                pilha.append(texto)
                pilha_refazer.clear() 
                exibir_texto()

def exibir_texto():
    x = " ".join(pilha)
    print("Documento de texto")
    print("-" * 20)
    print(x)
    print("-" * 20)

menu()

     