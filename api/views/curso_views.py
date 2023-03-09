from flask import jsonify, make_response, request
from flask_restful import Resource

from api import api

from ..entidades import curso
from ..schemas import curso_schemas
from ..services import curso_service

#400 - error of client
#500 - error of server


class CursoList(Resource):
    def get(self):
        return 'minha api esta funcionando ok'

    def post(self):
        cs = curso_schemas.CursosSchema()
        validade = cs.validate(request.json)
        if validade:
            return make_response(jsonify(validade), 400)
        else:
            nome = request.json["nome"]
            descricao = request.json["descricao"]
            data_publicacao = request.json["data_publicacao"]

            novo_curso = curso.Curso(nome=nome, descricao=descricao, data_publicacao=data_publicacao)
            resultado = curso_service.cadastrar_curso(novo_curso)
            x = cs.jsonify(resultado)
            return make_response(x, 201)
        

api.add_resource(CursoList, '/cursos')