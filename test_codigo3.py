from codigo3 import *

def test_soma_dobro(lista_simples):
    assert soma_dobro(lista_simples) == 30
    assert soma_dobro([0, 0, 0]) == 0
    assert soma_dobro([]) == 0
    assert soma_dobro([10]) == 20
    assert soma_dobro([-1, -2 , -3]) == -12