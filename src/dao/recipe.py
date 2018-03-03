import requests
import json
from src.model.model import RecipePuppyResponse, Recipe, Ingredient


class RecipeDao:
    def __init__(self):
        self.api = "http://www.recipepuppy.com/api/"
        self._format_path = "../../resources/ingredients.json"
        self._ingr_map = {}
        self.read_ingr_map()

    def read_ingr_map(self):
        with open(self._format_path, 'r') as file:
            self.ingr_map = json.load(file)

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
        ingredients = self._format_ingredients(ingredients)
        params = {}
        if missing_factor == 0:
            params["i"] = ",".join(self._format_ingredients(ingredients))
        elif missing_factor == 1:
            # ingredients.appennd("new ingredient")
            params["i"] = ",".join(self._format_ingredients(ingredients))
        # print(params)
        req = requests.get(self.api, params=params)
        data = req.json()
        return self._format_response(data["results"])

    def get_recipe_with_image(self):
        pass

    def get_recipe(self, name):
        pass


if __name__ == "__main__":
    dao = RecipeDao()
    result = dao.get_recipe_with_ingr(["onion", "garlic"])
    print(result)
