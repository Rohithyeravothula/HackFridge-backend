import requests
import json
from model.model import RecipePuppyResponse, Recipe, Ingredient
from integrations.imagerecog import ImageRecog

imgrc = ImageRecog()


class RecipeDao:
    def __init__(self):
        self.api = "http://www.recipepuppy.com/api/"
        self._format_path = "../resources/ingredients.json"
        self._ingr_map = {}
        self.read_ingr_map()

    def read_ingr_map(self):
        with open(self._format_path, 'r') as file:
            self._ingr_map = json.load(file)

    def _format_ingredients(self, ingredients):
        return list(map(lambda ing: self._ingr_map[ing]
        if ing in self._ingr_map else ing, ingredients))

    def _format_response(self, response):
        recipes = []
        for json_data in response:
            response_obj = RecipePuppyResponse.from_json(json_data)
            ingr = list(map(lambda istr: Ingredient(istr, "figure", None, "1"),
                            response_obj.ingredients.split(",")))
            recipes.append(Recipe(response_obj.title, "figure this our",
                                  "1", response_obj.thubnail, ingr))
        return recipes

    def get_recipe_with_ingr(self, ingredients, missing_factor=0):
        """
        :param ingredients: just names of the ingredients
        :param missing_factor: on how to search for recipes with missing
                                ingredients
        :return: recipes
        """
        # ingredients = self._format_ingredients(ingredients)
        ingredients = list(
            map(lambda ing: self._ingr_map[ing] if ing in self._ingr_map else ing, ingredients))
        # print(self._ingr_map.keys())
        params = {}
        if missing_factor == 0:
            params["i"] = ",".join(self._format_ingredients(ingredients))
        elif missing_factor == 1:
            params["i"] = ",".join(self._format_ingredients(ingredients))
        req = requests.get(self.api, params=params)
        # print(req.json())
        data = req.json()
        if data["results"]:
            return self._format_response(data["results"])
        print("empty results")
        return []

    def get_recipe_with_image(self, img_data):
        ingr = imgrc.get_ingredients(img_data)
        return self.get_recipe_with_ingr(ingr)

    def get_recipe(self, name):
        params = {"q": name}
        req = requests.get(self.api, params=params)
        data = req.json()
        return self._format_response(data["results"])


if __name__ == "__main__":
    dao = RecipeDao()
    recipe = dao.get_recipe("omlet")
    print(recipe)
