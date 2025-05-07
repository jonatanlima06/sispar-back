# Armazenar as configurações do ambiente de desenvolvimento
from os import environ # Esse arquivo tem acesso a variaveis de ambiente
from dotenv import load_dotenv # Permite o carregamento das variaveis de ambiente nesse arquivo

load_dotenv()

class Config():
    SQLALCHEMY_DATABASE_URI = environ.get('URL_DATABASE_PROD') # Puxa a variavel de ambiente e utiliza para a conexão
    SQLALCHEMY_TRACK_MODIFICATIONS=False # Otimiza as querys no banco de dados