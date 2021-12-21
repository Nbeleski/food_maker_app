from datetime import datetime

from main import db, ma

class Ingredient(db.Model):
    ingredient_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<Ingredient: %r>' % self.name

class IngredientSchema(ma.Schema):
    class Meta:
        fields = ('name', 'weight', 'price')
        model = Ingredient

ingredient_schema = IngredientSchema()
ingredients_schema = IngredientSchema(many=True)

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    weight = db.Column(db.Integer)
    price = db.Column(db.Float)

    def __repr__(self):
        return '<Product: %r>' % self.name

class ProductSchema(ma.Schema):
    class Meta:
        fields = ('name', 'weight', 'price')
        model = Product

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.ingredient_id'), nullable=False)
    ingredient_weight = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Recipe for product ID: %r>' % self.product_id

class RecipeSchema(ma.Schema):
    class Meta:
        fields = ('ingredient_id', 'ingredient_weight')
        model = Recipe

recipe_schema = RecipeSchema()
recipes_schema = RecipeSchema(many=True)

class IngredientListSchema(ma.Schema):
    class Meta:
        fields = ('name', 'ingredient_weight', 'cost')
        #model = Recipe

ingredient_list_schema = IngredientListSchema(many=True)