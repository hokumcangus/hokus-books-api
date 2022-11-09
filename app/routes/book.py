from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, abort, make_response, request

bp = Blueprint("books", __name__, url_prefix="/books")

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)
    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))

    return model

@bp.route("/<id>", methods=["GET"])
def handle_book(id):
    book = validate_model(Book, id)
    return jsonify(book.to_dict()), 200

@bp.route("", methods=["POST"])
def create_book():
    request_body = request.get_json()
    new_book = Book.from_dict(request_body)

    db.session.add(new_book)
    db.session.commit()

    return make_response(f"Book {new_book.title} successfully created", 201)

@bp.route("", methods=["GET"])
def read_all_books():
    title_query = request.args.get("title")
    description_query = request.args.get("description")
    limit_query = request.args.get("limit")

    book_query = Book.query

    if title_query:
        book_query = book_query.filter_by(title=title_query)

    if description_query:
        book_query = book_query.filter_by(description_query)

    if limit_query:
        book_query = book_query.limit(limit_query)

    books = book_query.all()

    books_response = [book.to_dict() for book in books]

    return jsonify(books_response)

@bp.route("/<id>", methods=["PUT"])
def update_book(id):
    book = validate_model(Book, id)
    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()
    return make_response(f"Book #{book.id} successfully updated"), 200

@bp.route("/<id>", methods=["DELETE"])
def delete_book(id):
    book = validate_model(Book, id)
    db.session.delete(book)
    db.session.commit()
    return make_response(f"Book #{book.id} successfully deleted"), 200