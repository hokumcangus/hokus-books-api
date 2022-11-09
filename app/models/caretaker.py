from app import db

class Caretaker(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    cats = db.relationship("Book", back_populates="caretaker")

    @classmethod
    def from_dict(cls, data_dict):
        return cls(title=data_dict["title"], description=["description"])

    def to_dict(self):
        return dict(
            id=self.id,
            title=self.title,
            description=self.description
        )
