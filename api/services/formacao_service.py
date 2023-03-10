from ..models import formacao_model
from api import db

def cadastrar_formacao(formacao):
    
    formacao = formacao_model.Formacao(nome=formacao.nome)
    db.session.add(formacao)
    db.session.commit()
    return formacao

def listar_formacao():
    formacao = formacao_model.Formacao.query.all()
    return formacao

def listar_formacao_id(id):
    formacao = formacao_model.Formacao.query.filter_by(id=id).first()
    return formacao

def atualiza_formacao(formacao_anterior, formacao_novo):
    formacao_anterior.nome = formacao_novo.nome
    formacao_anterior.descricao = formacao_novo.descricao
    db.session.commit()

def remove_formacao(formacao):
    db.session.delete(formacao)
    db.session.commit()