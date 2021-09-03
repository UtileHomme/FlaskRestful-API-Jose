from datetime import timedelta

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from resources.user import UserRegister

from security import authenticate, identity
from resources.item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'Jatin'
api = Api(app)

# changing the default token expiry time
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=30)
jwt = JWT(app, authenticate, identity)

api.add_resource(ItemList, '/items')

api.add_resource(Item, '/item/<string:name>')

api.add_resource(UserRegister, '/register')

# to avoid run this file in case of an import is done for app.py
if __name__ == '__main__':
    app.run(port=5000, debug=True)