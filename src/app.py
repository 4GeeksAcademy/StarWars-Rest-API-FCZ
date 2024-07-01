"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, Vehicles
import datetime
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/users', methods=['GET'])
def get_users():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


@app.route('/characters', methods=['GET'])
def get_characters():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


@app.route('/characters/<int:character_id>', methods=['GET'])
def get_single_character():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


@app.route('/planets', methods=['GET'])
def get_planets():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_single_planet():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


@app.route('/vehicles', methods=['GET'])
def get_vehicles():

    response_body = {
        "msg": "Hello, this is your GET /vehicles response "
    }

    return jsonify(response_body), 200


@app.route('/vehicles/<int:vehicle_id>', methods=['GET'])
def get_single_vehicle():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

@app.route('/users/favorites', methods=['GET'])
def get_user_favorites():

    response_body = {
        "msg": "Hello, this is your GET /user/favorites response "
    }

    return jsonify(response_body), 200

'''@app.route('/users/favorite_characters/<int:character_id>', methods=['POST'])
def get_single_favorite_character():

    request_body = request.get_json()
    
    added_character = {
        "id": id
    }

    return jsonify(added_character), 200

    response_body = {
        "msg": "The character was added to favorites!"
    }

    return jsonify(response_body), 200'''


@app.route('/users/favorite_characters/<int:character_id>', methods=['DELETE'])
def delete_favorite_character():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


@app.route('/users/favorite_planets', methods=['DELETE'])
def delete_favorite_planet():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


@app.route('/users/favorite_vehicles', methods=['DELETE'])
def delete_favorite_vehicle():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200

with app.app_context():
    existing_user = User.query.filter_by(email = 'mail@test.com').first()
    if not existing_user:
        new_user = User(
            username = 'User1',
            name = 'User',
            lastname = 'One',
            email = 'mail@test.com',
            subscription_date = datetime.datetime(2020, 5, 17),
            password = '123456'
        )
        db.session.add(new_user)
        db.session.commit()

with app.app_context():
    luke_skywalker = Characters.query.filter_by(name = 'Luke Skywalker').first()
    if not luke_skywalker:
        luke_skywalker = Characters(
            name = 'Luke Skywalker',
            age = 22,
            eye_color = 'Blue',
            hair_color = 'Blonde'
        )
        db.session.add(luke_skywalker)

    c3po = Characters.query.filter_by(name = 'C3PO').first()
    if not c3po:
        c3po = Characters(
            name = 'C3PO',
            age = 99,
            eye_color = 'Yellow',
            hair_color = 'None'
        )
        db.session.add(c3po)
    
        db.session.commit()





# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
