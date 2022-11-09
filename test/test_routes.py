from app.models.book import Book
from werkzeug.exceptions import HTTPException
from app.routes.book import validate_model
import pytest

def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()
    
    # Assert
    assert response.status_code == 200 
    assert response_body == []

def test_get_one_book_returns_book(client, one_saved_book):
    # act
    response = client.get("/books/1")
    response_body = response.get_json()

    # assert 
    assert response.status_code == 200 
    assert response_body["id"] == one_saved_book.id
    assert response_body["title"] == one_saved_book.title
    assert response_body["description"] == one_saved_book.description
    
def test_create_book_happy_path(client):
    # arrange
    EXPECTED_BOOK = {
        "title": "Three blind mice",
        "description": "wise"
    }
    
    response = client.post("/books", json=EXPECTED_BOOK)
    response_body = response.get_data(as_text=True)
    actual_book = Book.query.get(1)

    # assert
    assert response.status_code == 201
    assert response_body == f"Book {EXPECTED_BOOK['title']} successfully created"
    assert actual_book.title == EXPECTED_BOOK["title"]
    assert actual_book.description == EXPECTED_BOOK["description"]

# def test_get_one_book(client):
#     # Act
#     response = client.get("/books/1")
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 200
#     assert response_body == {
#         "id": "",
#         "title": "",
#         "description": ""
#     }

# def test_get_all_books_with_no_records(client):
#     # Act
#     response = client.get("/books")
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 200
#     assert response_body == []


# def test_to_dict_no_missing_data():
#     # Arrange
#     test_data = Book(id = 1,
#                     title="Ocean Book",
#                     description="watr 4evr")

#     # Act
#     result = test_data.to_dict()

#     # Assert
#     assert len(result) == 3
#     assert result["id"] == 1
#     assert result["title"] == "Ocean Book"
#     assert result["description"] == "watr 4evr"

# def test_to_dict_missing_id():
#     # Arrange
#     test_data = Book(title="Ocean Book",
#                     description="watr 4evr")

#     # Act
#     result = test_data.to_dict()

#     # Assert
#     assert len(result) == 3
#     assert result["id"] is None
#     assert result["title"] == "Ocean Book"
#     assert result["description"] == "watr 4evr"

# def test_to_dict_missing_title():
#     # Arrange
#     test_data = Book(id=1,
#                     description="watr 4evr")

#     # Act
#     result = test_data.to_dict()

#     # Assert
#     assert len(result) == 3
#     assert result["id"] == 1
#     assert result["title"] is None
#     assert result["description"] == "watr 4evr"

# def test_to_dict_missing_description():
#     # Arrange
#     test_data = Book(id = 1,
#                     title="Ocean Book")

#     # Act
#     result = test_data.to_dict()

#     # Assert
#     assert len(result) == 3
#     assert result["id"] == 1
#     assert result["title"] == "Ocean Book"
#     assert result["description"] is None

# def test_create_one_book(client):
#     # Act
#     response = client.post("/books", json={
#         "title": "New Book",
#         "description": "The Best!"
#     })
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 201
#     assert response_body == "Book New Book successfully created"

# def test_create_one_book_no_title(client):
#     #Arrange
#     test_data = {"description": "The Best!"}

#     #Act and Assert
#     with pytest.raises(KeyError, match='title'):
#         response = client.post("/books", json=test_data)
# def test_create_one_book_no_description(client):
#     # Arrange
#     test_data = {"title": "New Book"}

#     # Act & Assert
#     with pytest.raises(KeyError, match = 'description'):
#         response = client.post("/books", json=test_data)

# def test_create_one_book_with_extra_keys(client, two_saved_books):
#     # Arrange
#     test_data = {
#         "extra": "some stuff",
#         "title": "New Book",
#         "description": "The Best!",
#         "another": "last value"
#     }

#     # Act
#     response = client.post("/books", json=test_data)
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 201
#     assert response_body == "Book New Book successfully created"

# def test_update_book(client, two_saved_books):
#     # Arrange
#     test_data = {
#         "title": "New Book",
#         "description": "The Best!"
#     }

#     # Act
#     response = client.put("/books/1", json=test_data)
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 200
#     assert response_body == "Book #1 successfully updated"

# def test_update_book_with_extra_keys(client, two_saved_books):
#     # Arrange
#     test_data = {
#         "extra": "some stuff",
#         "title": "New Book",
#         "description": "The Best!",
#         "another": "last value"
#     }

#     # Act
#     response = client.put("/books/1", json=test_data)
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 200
#     assert response_body == "Book #1 successfully updated"

# def test_update_book_missing_record(client, two_saved_books):
#     # Arrange
#     test_data = {
#         "title": "New Book",
#         "description": "The Best!"
#     }

#     # Act
#     response = client.put("/books/3", json=test_data)
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 404
#     assert response_body == {"message": "book 3 not found"}

# def test_update_book_invalid_id(client, two_saved_books):
#     # Arrange
#     test_data = {
#         "title": "New Book",
#         "description": "The Best!"
#     }

#     # Act
#     response = client.put("/books/cat", json=test_data)
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 400
#     assert response_body == {"message": "book cat invalid"}

# def test_delete_book(client, two_saved_books):
#     # Act
#     response = client.delete("/books/1")
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 200
#     assert response_body == "Book #1 successfully deleted"

# def test_delete_book_missing_record(client, two_saved_books):
#     # Act
#     response = client.delete("/books/3")
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 404
#     assert response_body == {"message": "book 3 not found"}

# def test_delete_book_invalid_id(client, two_saved_books):
#     # Act
#     response = client.delete("/books/cat")
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 400
#     assert response_body == {"message": "book cat invalid"}

# def test_validate_book(two_saved_books):
#     # Act
#     result_book = validate_model(Book,1)

#     # Assert
#     assert result_book.id == 1
#     assert result_book.title == "Ocean Book"
#     assert result_book.description == "watr 4evr"

# def test_validate_book_missing_record(two_saved_books):
#     # Act & Assert
#     # Calling `validate_book` without being invoked by a route will
#     # cause an `HTTPException` when an `abort` statement is reached 
#     with pytest.raises(HTTPException):
#         result_book = validate_model(Book, "3")
    
# def test_validate_book(two_saved_books):
#     # Act
#     # Add `Book` argument to `validate_model` invocation
#     result_book = validate_model(Book, 1)

#     # Assert
#     assert result_book.id == 1
#     assert result_book.title == "Ocean Book"
#     assert result_book.description == "watr 4evr"
