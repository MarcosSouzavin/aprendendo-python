# ==========================================
# 1. ARMAZENAMENTO (A NOSSA GAVETA)
# ==========================================
# Aqui guardaremos todas as "fichas" (dicionários) dos alunos.
banco_de_dados = [] # --> Lista vazia para armazenar dados
# ==========================================
# 2. FERRAMENTAS (OS NOSSOS ROBÔS)
# ==========================================

def calcular_media(notas):
    """Soma as notas e divide pela quantidade delas."""
    return sum(notas) / len(notas)

def definir_status(media):
    """Analisa a média e retorna a situação do aluno."""
    if media >= 7.0:
        return "APROVADO"
    elif media >= 5.0:
        return "RECUPERAÇÃO"
    else:
        return "REPROVADO"\
# Esses robôs (funções) são como máquinas que fazem tarefas específicas.
# O calcular_media pega uma lista de notas, soma tudo 
# e divide pelo número de notas.
# O definir_status recebe a média e decide se o aluno 
# foi aprovado, está de recuperação ou reprovado.
# Você pode criar quantos robôs quiser para ajudar em outras 
# tarefas, como calcular a média
# de mais notas, ou até mesmo para formatar a saída de dados 
# de uma maneira diferente.
# Exemplo de outro robô:

def adicionar_aluno():
    """Lógica para ler dados, processar e guardar no banco."""
    print("\n--- Cadastro de Novo Aluno ---")
    nome = input("Digite o nome do aluno: ").strip().capitalize()
    
    # O bloco 'try' tenta executar o código. 
    # Se o usuário digitar bobagem, o 'except' avisa.
    # O 'float' tenta converter a entrada em número decimal,
    # se o usuário digitar algo que não é número, ele vai para o 'except
    try:
        n1 = float(input(f"Digite a primeira nota de {nome}: "))
        n2 = float(input(f"Digite a segunda nota de {nome}: "))
        
        # Chamando os robôs auxiliares
        # calcular a média e definir a situação do aluno
        # calcular_media é o robô que calcula a média das notas,
        # e definir_status é o robô que decide se o aluno foi aprovado,
        # está de recuperação ou reprovado, com base na média calculada.

        media_final = calcular_media([n1, n2])
        situacao = definir_status(media_final)
        
        # Criando a 'ficha' (Dicionário)
        # O dicionário 'aluno' é como uma ficha de cadastro, onde cada chave
        # representa um campo (nome, notas, média, status) e cada valor é a informação correspondente.
        # Por exemplo, a chave "nome" tem o valor do nome do aluno,
        # a chave "notas" tem uma lista com as notas, a chave "media"
        # tem a média calculada e a chave "status" tem a situação do aluno
        # (aprovado, recuperação ou reprovado).
        aluno = {
            "nome": nome,
            "notas": [n1, n2],
            "media": round(media_final, 2),
            "status": situacao
        }
        # O aluno é criado como um dicionário,
        # e depois é adicionado à lista banco_de_dados.
        # O banco_de_dados é a nossa "gaveta" onde
        # guardamos todas as fichas dos alunos.
        # O comando 'append' é usado para adicionar o dicionário do aluno
        # à lista banco_de_dados, ou seja,
        # ele guarda a ficha do aluno na nossa "gaveta".
        # Depois de adicionar o aluno,
        # o programa imprime uma mensagem de sucesso.
        

        # Guardando na lista
        banco_de_dados.append(aluno)
        print(f"\nSucesso! {nome} foi adicionado ao sistema.")
        # O comando 'append' é usado para adicionar o dicionário do aluno
        # à lista banco_de_dados, ou seja,
        # ele guarda a ficha do aluno na nossa "gaveta".
        # Depois de adicionar o aluno,
        # o programa imprime uma mensagem de sucesso.
        # O comando 'append' é usado para adicionar o dicionário do aluno
        # à lista banco_de_dados, ou seja,
        # ele guarda a ficha do aluno na nossa "gaveta".
        
    except ValueError:
        print("\nERRO: Você digitou algo que não é um número! Tente cadastrar novamente.")
        # O bloco 'except' captura o erro de conversão 
        # (ValueError) que ocorre quando o 
        # usuário digita algo que não pode ser convertido para float,
        # como letras ou símbolos. Ele então exibe uma mensagem de erro
        # e orienta o usuário a tentar cadastrar novamente.
def exibir_relatorio():
    """Mostra todos os alunos cadastrados de forma organizada."""
    print("\n" + "="*40)
    print(f"{'RELATÓRIO ESCOLAR':^40}") # O :^40 centraliza o texto
    print("="*40)
    # O 'if' verifica se o banco_de_dados está vazio. 
    # Se estiver, avisa que não há alunos.
    if not banco_de_dados:
        print("Ainda não há alunos no sistema.")
    else:
        # 'for' percorre a lista de alunos um por um
        for aluno in banco_de_dados:
            print(f"ALUNO: {aluno['nome']:<15} | MÉDIA: {aluno['media']:<5} | STATUS: {aluno['status']}")
    # O 'for' percorre a lista de alunos um por um, e para cada aluno,
    # ele imprime o nome, a média e o status de forma formatada.
    # O '<' na formatação indica que o texto deve ser alinhado à esquerda,
    # e o número após ele (15 para nome, 5 para média) define a largura do campo.
    print("="*40)

# ==========================================
# 3. INTERFACE (O PAINEL DE CONTROLE)
# ==========================================

def menu_principal():
    """O coração do programa. Mantém o sistema rodando."""
    while True:
        print("\n--- MENU DE CONTROLE ---")
        print("1. Cadastrar Aluno")
        print("2. Exibir Relatório")
        print("3. Sair do Sistema")
        
        opcao = input("\nO que deseja fazer? (1/2/3): ")
        
        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            exibir_relatorio()
        elif opcao == "3":
            print("\nFinalizando sistema... Até logo!")
            break # Encerra o 'while' e, consequentemente, o programa
        else:
            print("\nOpção inválida! Escolha 1, 2 ou 3.")

    # O menu_principal é o painel de controle do programa, onde o
    # usuário pode escolher o que fazer.
    # Ele usa um loop 'while True' para manter o programa rodando até que o
    # usuário escolha sair (opção 3). Dentro do loop, ele exibe
    # as opções do menu,
    # lê a escolha do usuário e chama a função correspondente 
    # (adicionar_aluno ou exibir_relatorio). Se o usuário escolher sair,
    # o programa imprime uma mensagem de despedida e quebra o loop,
    # encerrando o programa. Se o usuário digitar algo que não é uma 
    # opção válida, ele exibe uma mensagem de erro e volta a mostrar o menu.

# ==========================================
# 4. START (A IGNIÇÃO)
# ==========================================
# Esse comando diz: "Se este arquivo for o principal sendo executado, ligue o menu".
if __name__ == "__main__":
    menu_principal()
# O comando 'if __name__ == "__main__":' é 
# uma convenção em Python que verifica se o arquivo está
# sendo executado diretamente (como o programa principal) ou se
# está sendo importado como um módulo em outro arquivo. Se o 
# arquivo for executado diretamente, a condição será verdadeira e o código
# dentro desse bloco será executado, iniciando o programa. Se o arquivo for 
# importado, a condição será falsa e o código dentro do
# bloco não será executado, permitindo que as funções e variáveis 
# definidas no arquivo sejam usadas sem iniciar o programa automaticamente.
# Isso é útil para organizar o 
# código e evitar que partes do programa sejam executadas quando o
# arquivo é importado como um módulo em outro lugar.