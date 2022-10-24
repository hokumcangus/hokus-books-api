from crypt import methods
from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    my_beautiful_response_body = "Aloha Kakahi'aka"
    return my_beautiful_response_body, 200

@hello_world_bp.route("/hello/JSON", methods=["GET"])
def say_hello_json():
    return{
        "name": "Hoku",
        "message": "Wassup",
        "hobbies": ["music", "dancing", "family time"]
    }
