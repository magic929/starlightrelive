from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from models import dress
from models import chara

api_bp = Blueprint('api', __name__, url_prefix='/api')
parser = reqparse.RequestParser(trim=True)
parser.add_argument('strength', type=str, action='append')  
    
class Dress(Resource):
    def get(self):
        dresses = dress.get_random_id()
        for d in dresses:
            d['charaId'] = chara.get_id(d['charaId']).name
        return dresses

    def post(self):
        args = parser.parse_args()
        result = args["strength"]
        print(result)

api = Api(api_bp)
api.add_resource(Dress, '/dress')