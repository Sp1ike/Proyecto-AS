from flask_restful import Resource, reqparse
from flask import jsonify
from .models import db, Foro

parser = reqparse.RequestParser()
parser.add_argument('id_comunidad', type=int, required=True, help="ID de comunidad requerido")
parser.add_argument('id_usuario', type=int, required=True, help="ID de usuario requerido")
parser.add_argument('tipo_foro', type=str, required=True, help="Tipo de foro requerido")
parser.add_argument('estado_foro', type=str, required=True, help="Estado de foro requerido")
parser.add_argument('tema_foro', type=str, required=True, help="Tema de foro requerido")

class ForoListResource(Resource):
    def get(self):
        foros = Foro.query.all()
        return jsonify([foro.tema_foro for foro in foros])

    def post(self):
        args = parser.parse_args()
        nuevo_foro = Foro(
            id_comunidad=args['id_comunidad'],
            id_usuario=args['id_usuario'],
            tipo_foro=args['tipo_foro'],
            estado_foro=args['estado_foro'],
            tema_foro=args['tema_foro']
        )
        db.session.add(nuevo_foro)
        db.session.commit()
        return jsonify(nuevo_foro.tema_foro)

class ForoResource(Resource):
    def get(self, id):
        foro = Foro.query.get_or_404(id)
        return jsonify(foro.tema_foro)

    def put(self, id):
        args = parser.parse_args()
        foro = Foro.query.get_or_404(id)
        foro.id_comunidad = args['id_comunidad']
        foro.id_usuario = args['id_usuario']
        foro.tipo_foro = args['tipo_foro']
        foro.estado_foro = args['estado_foro']
        foro.tema_foro = args['tema_foro']
        db.session.commit()
        return jsonify(foro.tema_foro)

    def delete(self, id):
        foro = Foro.query.get_or_404(id)
        db.session.delete(foro)
        db.session.commit()
        return '', 204
