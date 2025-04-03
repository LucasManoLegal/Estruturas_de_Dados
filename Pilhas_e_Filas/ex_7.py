# Exercício 8 - Extra
# Um navegador de internet usa uma pilha para armazenar o histórico de
# navegação. Cada vez que o usuário acessa uma nova página, ela é adicionada
# ao histórico. O usuário pode voltar para a página anterior ou avançar
# novamente.
# • Crie uma pilha para armazenar as páginas visitadas.
# • Empilhe três páginas acessadas pelo usuário.
# • Mostre a última página visitada.
# • O usuário clica no botão "Voltar", então desempilhe a última página
# visitada e mostre a nova página no topo.
# • O usuário decide avançar novamente. Como o histórico de páginas
# acessadas foi modificado, implemente um sistema para refazer a
# navegação caso necessário.

historico_pilhas = []

historico_pilhas.append("Página 1 - Home")
historico_pilhas.append("Página 2 - Sobre nós")
historico_pilhas.append("Página 3 - Produtos")

ultima_pagina = historico_pilhas[-1]
print(f"A última página visitada foi: {ultima_pagina}")

pagina_voltar = historico_pilhas.pop() 
print(f"Voltando... A nova página no topo é: {historico_pilhas[-1]}")

historico_avancar = []

historico_avancar.append(pagina_voltar)  
print(f"Avançando... A página avançada foi: {historico_avancar[-1]}")

if historico_avancar:
    pagina_avancar = historico_avancar.pop()  
    print(f"Avançando... A página no topo do histórico de avançar é: {pagina_avancar}")
else:
    print("Não há mais páginas para avançar.")
