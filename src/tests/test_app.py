import pytest # Traz a biblioteca de testes
import time # manipular tempo
from src.model.colaborador_model import Colaborador
from src.app import create_app

#----------------------------Configurações para o teste-----------

@pytest.fixture #Identifica funções de configurações para o teste
def app():
    app = create_app()
    yield app
    
@pytest.fixture
def client(app):
    return app.teste_client()

#------------------------------------------------------------

def test_desempenho_requisicao_get(client):
    comeco = time.time() #pegar a hora atual e transformar em segundos
    
    for _ in range(100):
        resposta = client.get('/colaborador/todos-colaboradores')
        
    fim = time.time() - comeco
    
    assert fim < 1.0