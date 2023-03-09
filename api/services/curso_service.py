from ..models import curso_model
from api import db

def cadastrar_curso(curso):
    
    curso_bd = curso_model.Curso(nome=curso.nome, descricao=curso.descricao, data_publicacao=curso.data_publicacao)
    db.session.add(curso_bd)
    db.session.commit()
    return curso_bd