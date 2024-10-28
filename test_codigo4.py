from codigo4 import *

def test_acordar_cedo():
# Teste para falha de acordar_cedo
    assert acordar_cedo(7) == "Tente novamente amanhã"
# Teste para conclusão de acordar_cedo
    assert acordar_cedo(4) == "Você é um guerreiro"
# Teste se o tipo retornado na função acordar_cedo é str
#https://www.geeksforgeeks.org/python-isinstance-method/?ref=gcse_outind
    assert isinstance(acordar_cedo(4), str)

def test_tempo_exercicio():
# Teste para conclusão de tempo_exercicio
    assert tempo_exercicio(10, 3) == 9
#Teste para falha de tempo_exercicio
    assert tempo_exercicio(10, 2) == None
    assert tempo_exercicio(10, 1) == None

def test_tem_exercicio():
#Teste para verificar se se passar 'Descanso' em tem_exercicio
    assert tem_exercicio("Descanso") == False
# Teste para verificar se passar um esporte como parâmetro em tem_exercicio
    assert tem_exercicio("Treino") == True