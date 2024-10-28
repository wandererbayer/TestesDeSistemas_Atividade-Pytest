import pytest

def soma_dobro(numeros):
    return sum(x * 2 for x in numeros)

@pytest.fixture
def lista_simples():
    return [1, 2, 3, 4, 5]