from flask import jsonify, Blueprint
from flask import request
import Data
from flask_restful import Resource, Api, reqparse


class MinEng(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("id", required=True, help="No id provided", location=['form', 'json'])
        self.reqparse.add_argument("title", required=True, help="No title provided", location=['form', 'json'])
        self.reqparse.add_argument("data", required=True, help="No data provided", location=['form', 'json'])
        super(self.__class__, self).__init__()

    def get(self, query):
        args = request.args
        if 'title' in args:
            if 'data' in args:
                return jsonify(Data.get_double_search(args['title'], args['data']))
            return jsonify(Data.get_double_search(args['title'], None))
        return jsonify(Data.get_search(query))

    def post(self):
        args = self.reqparse.parse_args()
        Data.my_dict.append(args)
        print Data.my_dict
        return jsonify(args)


search_api = Blueprint('resources.MinEng', __name__)
api = Api(search_api)
api.add_resource(MinEng, "/search/<query>", endpoint='query')
api.add_resource(MinEng, "/index", endpoint='queries')
