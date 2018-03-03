from flask import Flask, jsonify
from flask import make_response
from dao import image,recipe
imageDA = image()
recipeDA = recipe()

handler = Flask(__name__)
@handler.route('/recipe/search',methods=['POST'])
def search():
    return recipeDA.get_recipe_with_ingredients()

@handler.route('/recipe/search/image',methods=['POST'])
def searchImages():
    return recipeDA.get_recipe_with_image()

@handler.route('/recipe/search/ingredients',methods=['POST'])
def searchIngredients():
    return imageDA.get_image_ingredients()

@handler.errorhandler(404)
def notfound(error):
    return make_response(jsonify({'error':'Not found'}),404)