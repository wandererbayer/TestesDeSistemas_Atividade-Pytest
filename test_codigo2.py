from codigo2 import *

def test_soma():
    assert soma(3, 4) == 7
    assert soma(-1, 1) == 0

def test_subtrai():
    assert subtrai(10, 5) == 5
    assert subtrai(0, 5) == -5

def test_multiplica():
    assert multiplica(3, 5) == 15
    assert multiplica(-1, 5) == -5

def test_divide():
    assert divide(10, 2) == 5
    assert divide(10, 0) == "Erro: divisão por zero não permitida."

def test_area_circulo():
    assert area_circulo(3) == math.pi * 9
    assert area_circulo(-1) == "Erro: o raio não pode ser negativo."

def test_area_retangulo():
    assert area_retangulo(5, 4) == 20
    assert area_retangulo(-1, 5) == "Erro: largura e altura devem ser não-negativos."