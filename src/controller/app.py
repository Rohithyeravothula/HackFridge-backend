from flask import Flask, jsonify, request, abort
from flask import make_response
from src.dao.image import ImageDao
from src.dao.recipe import RecipeDao
from src.util.utils import recipe_list_json, level1_list_json
from src.integrations.amazon import AmazonIntegration
from OpenSSL import SSL


context = SSL.Context(SSL.SSLv23_METHOD)
# context.use_privatekey_file()
# context.use_certificate_file("../../resources/ssl-cert/hacktech.crt")

imageDao = ImageDao()
recipeDao = RecipeDao()
amazonIR = AmazonIntegration()


app = Flask(__name__)


@app.route('/recipe/search', methods=['POST'])
def search():
    if not request.json:
        abort(400)
    content = request.json
    recipe_name = content["recipe"]
    return make_response(jsonify(recipe_list_json(recipeDao.get_recipe(recipe_name))))


@app.route('/recipe/search/image', methods=['POST'])
def search_images():
    if not request.json:
        abort(400)
    content = request.json
    img_data = content.get("image")
    return make_response(jsonify(recipe_list_json(recipeDao.get_recipe_with_image(img_data))))


@app.route('/recipe/search/ingredients', methods=['POST'])
def search_ingredients():
    if not request.json:
        abort(400)
    content = request.json
    ingredients = content["ingredients"]
    recipes = recipeDao.get_recipe_with_ingr(ingredients)
    return make_response(jsonify(recipe_list_json(recipes)))


@app.errorhandler(404)
def notfound(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route("/amazon/product/<name>")
def test_amazon(name):
    return make_response(jsonify(level1_list_json(amazonIR.get_products(name))))


@app.route("/search/test")
def test_endpoint():
    return make_response(jsonify({"key": "awesome"}))


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True, ssl_context=context)
