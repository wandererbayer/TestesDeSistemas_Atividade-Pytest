import math

# Função de verificação de email
def email_valido(email):
    return '@' in email and '.' in email

# Função para verificar se um número é par
def eh_par(n):
    return n % 2 == 0

# Função para calcular o fatorial
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)

# Função para calcular o quadrado
def quadrado(n):
    return n ** 2

# Função para verificar se o número é positivo
def eh_positivo(n):
    return n > 0

# Função para verificar a maioridade
def verificar_maioridade(idade):
    if idade >= 18:
        return 'maior de idade'
    else:
        return 'menor de idade'

# Função para classificar a temperatura
def classificar_temperatura(temp):
    if temp < 0:
        return 'frio'
    elif 0 <= temp <= 25:
        return 'moderado'
    else:
        return 'quente'

# Função para avaliar uma nota
def avaliar_nota(nota):
    if nota >= 7:
        return 'aprovado'
    elif 5 <= nota < 7:
        return 'recuperacao'
    else:
        return 'reprovado'

# Função para verificar se pode votar
def pode_votar(idade):
    if idade >= 18:
        return 'voto obrigatório'
    elif 16 <= idade < 18:
        return 'voto facultativo'
    else:
        return 'não pode votar'

# Função para avaliar um produto com base nas estrelas
def avaliar_produto(estrelas):
    if estrelas == 5:
        return 'excelente'
    elif estrelas == 4:
        return 'bom'
    elif estrelas == 3:
        return 'regular'
    elif estrelas == 2:
        return 'ruim'
    elif estrelas == 1:
        return 'péssimo'
    else:
        return 'valor inválido'
