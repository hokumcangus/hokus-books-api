import re
from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request, abort

books_bp = Blueprint("books", __name__, url_prefix="/books")
      
def validate_model(cls,model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__}{model_id} invalid"}, 400))
    model = cls.query.get(model_id)
    # for model in books:
    #     if model.id == book_id:
    #         return model
    if not model:
        abort(make_response({"message":f"model {model_id} not found"}, 404))
    return model

@books_bp.route("", methods=["GET"])
def read_all_books():
    
    title_query = request.args.get("title")
    if title_query:
        books = Book.query.filter_by(title=title_query)
    else:
        books = Book.query.all()

    books_response = []
    for book in books:
        books_response.append(book.to_dict())
    return jsonify(books_response)

@books_bp.route("/<book_id>", methods=["GET"])
def read_one_book(book_id):
    book = validate_model(book_id)
    return book.to_dict()

@books_bp.route("", methods=["POST"])
def create_books():
    request_body = request.get_json()
    new_book = Book(
        title=request_body["title"],
        description=request_body["description"])

    db.session.add(new_book)
    db.session.commit()

    return f"Book {new_book.title} successfully created", 201

@books_bp.route("/<book_id>", methods=["PUT"])
def update_book(book_id):
    book = validate_model(book_id)
    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()

    return make_response(f"Book #{book_id} succesfully updated")

@books_bp.route("/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = validate_model(book_id)

    db.session.delete(book)
    db.session.commit()

    return make_response(f"Book #{book_id} succesfully Deleted")
# hello_world_bp = Blueprint("hello_world", __name__)

# @hello_world_bp.route("/hello-world", methods=["GET"])
# def say_hello_world():
#     my_beautiful_response_body = "Aloha Kakahi'aka"
#     return my_beautiful_response_body, 200

# @hello_world_bp.route("/hello/JSON", methods=["GET"])
# def say_hello_json():
#     return{
#         "name": "Hoku",
#         "message": "Wassup",
#         "hobbies": ["music", "dancing", "family time"]
#     }, 404

# @hello_world_bp.route("/broken-endpoint-with-broken-server-code")
# def broken_endpoint():
#     response_body = {
#         "name": "Hoku",
#         "message": "Wassup",
#         "hobbies": ["music", "dancing", "family time"]
#     }
#     new_hobby = "Surfing"
#     response_body["hobbies"].append(new_hobby)
#     return response_body

# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "Harry Potter", "A Magic School"),
#     Book(2, "Hocus Pocus", "A Story about 3 Witches"),
#     Book(3, "Hubbie Halloween", "A Funny Halloween Movie")
#     ]


# INSERT INTO book
# VALUES (1,'A Wrinkle in Time', 'Fantastical');


# CREATE TABLE author (
#   id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
#   name TEXT,
#   books TEXT 
# );
# CREATE TABLE author (
#   id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
#   title VARCHAR(32),
#   description TEXT,
#   author_id INT,
#   FOREIGN KEY (author_id) REFERENCES book(id)
# );
