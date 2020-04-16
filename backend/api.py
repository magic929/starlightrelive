from flask import Blueprint
from flask_restful import Api, Resource, reqparse
from models.dress import get_id

api_bp = Blueprint('api', __name__, url_prefix='/api')
parser = reqparse.RequestParser(trim=True)
parser.add_argument('streth', type=dict, action='append')  
    
class Spam(Resource):
    def get(self):
        dress = get_id("1030003")
        return [{'name': dress.name, 'charaId': dress.chara_id}]
    
    def post(self):
        args = parser.parse_args()
        print("akb48")
        result = args["streth"]
        print(result)

api = Api(api_bp)
api.add_resource(Spam, '/dress')