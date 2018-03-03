from flask import Flask, jsonify, request, abort
from flask import make_response
from src.dao.image import ImageDao
from src.dao.recipe import RecipeDao
from src.util.utils import level1_list_json

imageDao = ImageDao()
recipeDao = RecipeDao()

app = Flask(__name__)


@app.route('/recipe/search', methods=['POST'])
def search():
    return recipeDao.get_recipe_with_ingr([], 0)


@app.route('/recipe/search/image', methods=['POST'])
def search_images():
    return recipeDao.get_recipe_with_image()


@app.route('/recipe/search/ingredients', methods=['POST'])
def search_ingredients():
    if not request.json:
        abort(400)
    content = request.json
    ingredients = content["ingredients"].split(",")
    recipes = recipeDao.get_recipe_with_ingr(ingredients)
    return make_response(jsonify(level1_list_json(recipes)))


@app.errorhandler(404)
def notfound(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route("/search/test")
def test_endpoint():
    return make_response(jsonify({"key": "awesome"}))


if __name__ == "__main__":
    app.run(debug=True)
