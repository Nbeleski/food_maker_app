from flask import Flask, current_app

from flask_restful import Api, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)

# routes imports precisam de db, ma e api criados
from routes.User import UserList, UserDetails
from routes.Recipes import IngredientList, ProductList, RecipeDetails, RecipeDetailsByName

@app.route("/")
@app.route("/index.html")
def index_html():
    return current_app.send_static_file('index.html')

api.add_resource(UserList, '/users')
api.add_resource(UserDetails, '/users/<username>')

api.add_resource(IngredientList, '/ingredients')
api.add_resource(ProductList, '/products')

api.add_resource(RecipeDetails, '/recipes/<int:id>')
api.add_resource(RecipeDetailsByName, '/recipes/<string:name>')