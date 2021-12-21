from flask import abort
from flask_restful import reqparse, abort, Api, Resource

from main import app, api
from models.Recipes import *
#from models.Recipes import recipes_schema

class IngredientList(Resource):
    def get(self):
        ingredients = Ingredient.query.all()
        return {'ingredients': ingredients_schema.dump(ingredients)}

class ProductList(Resource):
    def get(self):
        products = Product.query.all()
        return {'products': products_schema.dump(products)}

class RecipeDetails(Resource):
    def get(self, id):
        ingredients = Recipe.query.join(Ingredient, Recipe.ingredient_id==Ingredient.ingredient_id)\
            .with_entities(Ingredient.name, Recipe.ingredient_weight, (Ingredient.price * Recipe.ingredient_weight / Ingredient.weight)\
            .label('cost')).filter(Recipe.product_id==id)
        
        ingredient_list = ingredient_list_schema.dump(ingredients)
        if len(ingredient_list) == 0:
            return {'error': 'product not found'}, 404

        total_weight = sum([x['ingredient_weight'] for x in ingredient_list])
        total_cost = sum([x['cost'] for x in ingredient_list])

        return {'total_weight': total_weight, 'total_cost': total_cost, 'ingredient_list': ingredient_list}
        
class RecipeDetailsByName(Resource):
    def get(self, name):
        ingredients = Recipe.query.join(Ingredient, Recipe.ingredient_id==Ingredient.ingredient_id)\
            .join(Product, Product.product_id == Recipe.product_id)\
            .with_entities(Ingredient.name, Recipe.ingredient_weight, (Ingredient.price * Recipe.ingredient_weight / Ingredient.weight)\
            .label('cost')).filter(Product.name==name)
        
        ingredient_list = ingredient_list_schema.dump(ingredients)
        if len(ingredient_list) == 0:
            return {'error': 'product not found'}, 404

        total_weight = sum([x['ingredient_weight'] for x in ingredient_list])
        total_cost = sum([x['cost'] for x in ingredient_list])

        return {'total_weight': total_weight, 'total_cost': total_cost, 'ingredient_list': ingredient_list}
        

    