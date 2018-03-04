from model.model import RestRecipe

def recipe_list_json(lst):
    return list(map(lambda o: RestRecipe.to_Rest(o).__dict__ , lst))

def level1_list_json(lst):
    return list(map(lambda o: o.__dict__, lst))
