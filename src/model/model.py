import re

def whitespace_strip(inp):
    return " ".join(inp.split())


class Recipe:
    def __init__(self, name, type, serving, image_path, ingredients=None):
        self.name = name
        self.type = type
        self.serving = serving
        self.image_path = image_path
        self.ingredients = ingredients

    def __repr__(self):
        return "{} {} {}".format(self.name, self.type, self.ingredients)


class RestRecipe(Recipe):
    def __init__(self, name, type, serving, image_path, ingr_str):
        super(RestRecipe, self).__init__(name, type, serving, image_path, ingr_str)

    @staticmethod
    def to_Rest(recipe):
        return RestRecipe(recipe.name, recipe.type, recipe.serving, recipe.image_path,
                          ",".join(list(map(lambda x: x.name, recipe.ingredients))))



class Ingredient:
    def __init__(self, name, type, image, serving=None):
        self.name = name
        self.type = type
        self.image = image
        self.serving = serving

    def __repr__(self):
        return "({}, {})".format(self.name, self.type)



class RecipePuppyResponse:
    def __init__(self, title, href, ingredients, thumbnail):
        self.title = title
        self.href = href
        self.ingredients = ingredients
        self.thubnail = thumbnail

    @staticmethod
    def from_json(json_data):
        args = [json_data["title"], json_data["href"],
                                   json_data["ingredients"], json_data["thumbnail"]]
        args = list(map(lambda ele: whitespace_strip(ele), args))
        return RecipePuppyResponse(args[0], args[1], args[2], args[3])


class Product:
    def __init__(self, name, thumbnail, link, price):
        self.name = name
        self.thumbnail = thumbnail
        self.link = link
        self.price = price

    def __repr__(self):
        return "{} {}".format(self.name, self.price)


