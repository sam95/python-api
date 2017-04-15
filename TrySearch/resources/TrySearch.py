from flask import jsonify, Blueprint
from flask_restful import Resource, Api, reqparse
from module import search_google, search_duckgo, search_twitter


class TrySearch(Resource):
    def __init__(self):
        super(self.__class__, self).__init__()

    def get(self, query):
        my_dict = {"query": query, "results": {}}
        my_dict["results"]["google"] = {"text" : search_google(query)}
        my_dict["results"]["duckduckgo"] = {"text" : search_duckgo(query)}
        my_dict["results"]["twitter"] = {"text" : search_twitter(query)}
        return jsonify(my_dict)


search_api = Blueprint('resources.TrySearch', __name__)
api = Api(search_api)
api.add_resource(TrySearch, "/<query>", endpoint='query')
