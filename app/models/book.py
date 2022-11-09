from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)

    def to_dict(self):
        book_as_dict = {}
        book_as_dict["id"] = self.id
        book_as_dict["title"] = self.title
        book_as_dict["description"] = self.description

        return book_as_dict

    @classmethod
    def from_dict(cls, task_data):
        new_book = Book(title=task_data["title"], description=task_data["description"])
        return new_book