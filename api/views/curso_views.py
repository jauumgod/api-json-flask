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
        cursos = curso_service.listar_cursos()
        cs = curso_schemas.CursosSchema(many=True)
        return make_response(cs.jsonify(cursos),200)

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


class CursoDetail(Resource):
    def get(self, id):
        curso = curso_service.listar_curso_id(id)
        if curso is None:
            return make_response(jsonify("requisicao nao encontrado."),404)
        else:
            cs=curso_schemas.CursosSchema()
            return make_response(cs.jsonify(curso), 200)

    def put(self, id):
        curso_db = curso_service.listar_curso_id(id)
        if curso_db is None:
            return make_response(jsonify("curso nao foi encontrado."), 404)
        else:
            cs=curso_schemas.CursosSchema()
            validate = cs.validate(request.json)
        
        if validate:
            return make_response(jsonify(validate), 400)


    def delete(self, id):
        pass


api.add_resource(CursoList, '/cursos')
api.add_resource(CursoDetail, '/cursos/<int:id>')