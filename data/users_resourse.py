from flask_restful import Resource
from data import db_session
from data.result import Result
from flask import abort, jsonify
from data.user_parse import parser
from werkzeug.security import generate_password_hash


class ResListResource(Resource):
    def post(self):
        args = parser.parse_args()
        session = db_session.create_session()
        user = Result()
        user.nickname = args['nickname']
        user.set_password(args['result'])
        session.add(user)
        session.commit()
