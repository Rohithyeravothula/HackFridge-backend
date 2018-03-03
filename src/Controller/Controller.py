from flask import Flask, jsonify
from flask import make_response

handler = Flask(__name__)

@handler.route('/recipe/search')
def search():
    return ""

@handler.route('/recipe/search/image')
def searchImages():
    return ""

@handler.route('/recipe/search/ingredients')
def searchIngredients():
    return ""

@handler.errorhandler(404)
def notfound(error):
    return make_response(jsonify({'error':'Not found'}),404)