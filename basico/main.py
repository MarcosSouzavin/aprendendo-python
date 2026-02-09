# Ola, meu nome é Marcos e eu tenho 18 anos, esse arquivo tem objetivo de te ajudar 
# a melhorar as habilidades de programação, 
# e também me ajudar a aprender novas linguagens de programação, começarei do começo
# para ajudar novos programadores a aprenderem também. Espero que esse projeto seja útil :D

#tags (inicio de tudo)

nome = "Marcos"
idade = 18

# Imprime uma mensagem de saudação usando as variáveis nome e idade
print(f"Olá, meu nome é {nome} e eu tenho {idade} anos.")

# agora utilizando funções e logica de programação

idade >= 18 
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

# agora logica de repetição
for i in range(5):
    print(f"Contagem: {i}")

    # planilha para entender melhor as fases do estudo em python
# https://docs.google.com/spreadsheets/d/1m3IqPlWh-GNxxTw6HcvFlBX3pV2u94wRiM-IJAlpWXY/edit?usp=sharing

# vamos focar como o python armazena e organiza dados.

# Uma variável comum guarda um valor. Uma Lista guarda vários

# Exemplo de variável comum;

frutas = ["maçã", "banana", "laranja"]
frutas.append("uva")  # Adiciona "uva" à lista de frutas
print(frutas[0])  # imprime a fruta escolhida, 0 faz ele começar do começo da lista, ou seja, a maçã.

# Exemplo de dicionário, que é uma estrutura de dados que armazena pares de chave-valor.

usuario = {
    "nome": "Marcos",  
    "idade": 18,
    "cidade": "Sorocaba"
}

print(usuario["nome"])  

# Voce tem uma lista de chaves, e cada chave 
# tem um valor, nesse caso a chave "nome" tem o valor "Marcos".
# exemplo logico; 
# um banco de dados é como 
# um dicionário, onde cada chave é um campo como
# ("nome", "idade", etc.) e cada valor é a informação 
# correspondente para aquele campo.


# Acesse o arquivo: pratic.py para exercitar o que foi aprendido aqui.