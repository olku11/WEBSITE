from flask_restful import reqparse
import sqlalchemy

parser = reqparse.RequestParser()
parser.add_argument('nickname', required=True)
parser.add_argument('result', required=True)