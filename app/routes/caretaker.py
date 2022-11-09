from app import db
from app.models.caretaker import Caretaker
from app.models.book import Book
from flask import Blueprint, jsonify, abort, make_response, request

bp = Blueprint("caretakers", __name__, url_prefix="/caretakers")


def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response(
            {"message": f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)
    if not model:
        abort(make_response(
            {"message": f"{cls.__name__} {model_id} not found"}, 404))

    return model


@bp.route("", methods=["POST"])
def create_caretaker():
    request_body = request.get_json()
    new_caretaker = Caretaker.from_dict(request_body)

    db.session.add(new_caretaker)
    db.session.commit()

    return make_response(f"Caretaker {new_caretaker.name} successfully created", 201)


@bp.route("", methods=["GET"])
def read_all_caretakers():
    caretakers = Caretaker.query.all()

    caretakers_response = [caretaker.to_dict() for caretaker in caretakers]

    return jsonify(caretakers_response)


@bp.route("/<caretaker_id>/books", methods=["POST"])
def create_book(caretaker_id):
    caretaker = validate_model(Caretaker, caretaker_id)
    request_body = request.get_json()
    new_book = Book.from_dict(request_body)
    new_book.caretaker = caretaker

    db.session.add(new_book)
    db.session.commit()

    return make_response(f"Book {new_book.name} cared for by {caretaker.name}", 201)


@bp.route("/<caretaker_id>/books", methods=["GET"])
def read_book(caretaker_id):
    caretaker = validate_model(Caretaker, caretaker_id)

    books_response = []
    for book in caretaker.cats:
        books_response.append(book.to_dict())

    return(jsonify(books_response))
