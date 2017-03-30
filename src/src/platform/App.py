import datetime
import json
import os
from urllib.parse import urlparse, urljoin

from flask import Flask, redirect, render_template, request, abort, jsonify, url_for
from flask_login import LoginManager, login_required, login_user, current_user
from src.src.platform.Error import Error
from src.src.platform.InvalidUsage import InvalidUsage
from wtforms import Form, StringField, PasswordField
import warnings

from config.Config import Config
from src.src.db.Mysql import Config as Mysql_config
from src.src.controllers.model_controllers.EntityController import EntityController
from src.src.controllers.model_controllers.UserController import UserController
from src.src.controllers.service_controllers.SoundcloudController import SoundcloudController
from src.src.controllers.service_controllers.SpotifyController import SpotifyController
from src.src.controllers.service_controllers.TwitterController import TwitterController

if Config.TEST_ENV:
    app = Flask(__name__)
else:
    app = Flask(__name__, template_folder="/src/src/platform/templates", static_folder="/src/src/platform/static")
login_manager = LoginManager()
login_manager.init_app(app)

json.JSONEncoder.default = lambda self, obj: (obj.isoformat() if isinstance(obj, datetime.datetime) else None)


@login_manager.user_loader
def load_user(user_id):
    return UserController.get_by_id(id=user_id)


class LoginForm(Form):
    username = StringField('Username')
    password = PasswordField('Password')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        if UserController.login_user(request):
            user = UserController.get_by_email(request.form["email"])
            login_user(user)
            next_url = request.args.get('next')
            if not is_safe_url(next_url):
                return abort(400)
            return redirect(next_url or url_for('dashboard'))
        return render_template('login.html')
    else:
        raise InvalidUsage("Invalid Method", status_code=401)


@app.route("/logout")
@login_required
def logout():
    UserController.logout_user()
    return redirect(url_for('login'))


@app.route('/dashboard', methods=['GET'])
@login_required
def dashboard():
    entities = EntityController.get_approved_entities(current_user)
    return render_template('dashboard.html', entities=entities)


@app.route('/entity/data', methods=['GET'])
def get_entity_data():
    ent_id = request.args.get('id')
    data_dict = {
        "soundcloud_data": SoundcloudController.get_delta(int(ent_id)),
        "spotify_data": SpotifyController.get_delta(int(ent_id)),
        "twitter_data": TwitterController.get_delta(int(ent_id))
    }
    return jsonify(data_dict)


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


@app.route('/create/entity', methods=['POST'])
def create_entity():
    if request.method == 'POST':
        entity = EntityController.create_new_entity(request)
        if type(entity) is not Error:
            json_entity = json.dumps(entity.__dict__["_data"])
            return json_entity
        else:
            raise InvalidUsage(entity["error"], status_code=400)
    else:
        raise InvalidUsage("Invalid Method", status_code=401)


@app.route('/update/entity', methods=['POST'])
def update_entity():
    if request.method == 'POST':
        entity = EntityController.update_entity(request)
        if type(entity) is not Error:
            json_entity = json.dumps(entity.__dict__["_data"])
            return json_entity
        else:
            raise InvalidUsage(entity["error"], status_code=400)
    else:
        raise InvalidUsage("Invalid Method", status_code=401)


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


if __name__ == "__main__":
    if not Mysql_config.TEST_ENV:
        warnings.warn("In Production ENV/DATABASE", Warning)
    app.secret_key = os.urandom(12)
    app.run(debug=True, host='0.0.0.0', port=4000)
