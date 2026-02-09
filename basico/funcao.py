#  Definição de uma função em Python: 

def saudar_usuario(nome):
    return f"Olá, {nome}! Vamos programar?"

mensagem = saudar_usuario("Dev")
print(mensagem)
# A função saudar_usuario recebe um parâmetro
# nome e retorna uma mensagem de saudação personalizada.
# Você pode chamar essa função com diferentes 
# nomes para obter saudações personalizadas.
# uma personalizada por exemplo: 
def msg(mensagem):
    return f"Mensagem personalizada: {mensagem}"
recado = msg("Bem-vindo ao estudo de Python!")
print(recado)
# A função msg recebe um parâmetro mensagem
# e retorna uma string formatada com a mensagem personalizada
#----------------------------------------------------------------
# mais funcoes para praticar:
def calcular_area_circulo(raio):
    import math
    area = math.pi * (raio ** 2)
    return area
raio = 5
area = calcular_area_circulo(raio)
print(f"A área do círculo com raio {raio} é: {area:.2f}")
# A função calcular_area_circulo recebe o raio de um círculo
# e retorna a área calculada usando a fórmula A = πr².
# Você pode chamar essa função com 
# diferentes valores de raio para obter a área correspondente.
# import math é uma biblioteca que fornece funções matemáticas,
# como o valor de π (math.pi) e outras operações matemáticas.
