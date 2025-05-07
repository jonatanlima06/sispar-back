from src.model import db # Traz a instância do SQLAlchemy para esse arquivo
from sqlalchemy.schema import Column # essa linha vai trazer o recurso necessário para o ORM entender que o atributo será uma coluna na tabela
from sqlalchemy.types import String, DECIMAL, Integer # Importando tipos de dados que as colunas vão aceitar

class Colaborador(db.Model):
    
    
#--------------------------------ATRIBUTOS---------------------
    # nome VARCHAR(100)
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    email = Column(String(100))
    senha = Column(String(50))
    cargo = Column(String(100))
    salario = Column(DECIMAL(10,2))

#-------------------------------CONSTRUTOR---------------------

    def __init__(self, nome, email, senha, cargo, salario):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo
        self.salario = salario
#--------------------------------------------------------------

    def to_dict(self) -> dict:
        return {
            'email': self.email,
            'senha': self.senha,
        }
        
    def all_data(self) -> dict:
           return{
               'id': self.id,
               'nome': self.nome,
               'cargo': self.cargo,
               'salario': self.salario,
               'email': self.email
           }