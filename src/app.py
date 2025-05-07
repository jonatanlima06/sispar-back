# Responsável por criar a aplicação

from flask import Flask
from flask_cors import CORS
from src.controller.colaborador_controller import bp_colaborador
from src.model import db
from config import Config
from flasgger import Swagger

swagger_config = {
    "headers": [],
    "specs": [
        {
           "endpoint": 'apispec',
           "route": '/apispec.json',
           "rule_filter": lambda rule: True,
           "model_filter": lambda tag: True 
        }
    ],
    "static_url_path": '/flasgger_static',
    "static_ui": True,
    "specs_route": '/apidocs/'  
}

def create_app():
    app = Flask(__name__)
    CORS(app, origins=['*'])
    app.register_blueprint(bp_colaborador)
    
    app.config.from_object(Config)
    
    db.init_app(app) # Inicia a conexão com o banco de dados
    Swagger(app, config=swagger_config) 
    with app.app_context(): #Se as tabelas não existem, crie.
        db.create_all()
    
    return app
