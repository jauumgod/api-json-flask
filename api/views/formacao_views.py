from flask import jsonify, make_response, request
from flask_restful import Resource

from api import api

from ..entidades import formacao
from ..schemas import formacao_schemas
from ..services import formacao_service

#400 - error of client
#500 - error of server


class FormacaoList(Resource):
    def get(self):
        formacoes = formacao_service.listar_formacao()
        fs = formacao_schemas.FormacaoSchema(many=True)
        return make_response(fs.jsonify(formacoes),200)

    def post(self):
        fs = formacao_schemas.FormacaoSchema()
        validade = fs.validate(request.json)
        if validade:
            return make_response(jsonify(validade), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]

            nova_formacao = formacao.Formacao(nome=nome, descricao=descricao)
            resultado = formacao_service.cadastrar_formacao(nova_formacao)
            x = fs.jsonify(resultado)
            return make_response(x, 201)


class FormacaoDetail(Resource):
    def get(self, id):
        formacoes = formacao_service.listar_formacao_id(id)
        if formacoes is None:
            return make_response(jsonify("requisicao nao encontrado."),404)
        else:
            fs=formacao_schemas.FormacaoSchema()
            return make_response(fs.jsonify(formacoes), 200)

    def put(self, id):
        formacao_bd = formacao_service.listar_formacao_id(id)
        if formacao_bd is None:
            return make_response(jsonify("requisicao nao foi encontrado."), 404)
        else:
            fs=formacao_schemas.FormacaoSchema()
            validate = fs.validate(request.json)
        
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            nova_formacao = formacao.Formacao(nome=nome,descricao=descricao)
            formacao_service.atualiza_formacao(formacao_bd, nova_formacao)
            formacao_atualizada = formacao_service.listar_formacao_id(id)
            return make_response(fs.jsonify(formacao_atualizada), 200)

    def delete(self, id):
        formacao_bd = formacao_service.listar_formacao_id(id)
        if formacao_bd is None:
            return make_response(jsonify("requisicao nao encontrado."), 404)
        else:
            formacao_service.remove_formacao(formacao_bd)
            return make_response(jsonify("requisicao excluido com sucesso!"), 204)
        

api.add_resource(FormacaoList, '/formacao')
api.add_resource(FormacaoDetail, '/formacao/<int:id>')