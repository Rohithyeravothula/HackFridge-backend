class Recipe:
    def __init__(self, name, type, serving, image_path):
        self.name = name
        self.type = type
        self.serving = serving
        self.image_path = image_path



class Ingredient:
    def __init__(self, name, type, image, serving=None):
        self.name = name
        self.type = type
        self.image = image
        self.serving = serving
