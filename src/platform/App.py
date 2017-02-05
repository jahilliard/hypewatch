from flask import Flask, request, jsonify
from src.platform.InvalidUsage import InvalidUsage
from src.controllers.model_controllers.EntityController import EntityController
app = Flask(__name__)


@app.route('/create/entity', methods=['POST'])
def create_entity():
    if request.method == 'POST':
        entity = EntityController.create_new_entity(request)
        if "error" not in entity:
            return entity
        else:
            raise InvalidUsage(entity["error"], status_code=400)


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route('/update/entity', methods=['POST'])
def update_entity():
    return 'Hello, World!'


if __name__ == "__main__":
    app.run()
