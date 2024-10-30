#aqui são informadas as classes que incluem as tabelas no banco de dados

from app import db
from datetime import datetime

class Tarefas(db.Model):
    __nometabela__ = 'tarefas'
    
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    criacao = db.Column(db.DateTime, default=datetime.utcnow)
    concluida = db.Column(db.Boolean, default=False)
    
    def marcar_completa(self):
        self.completa = True



