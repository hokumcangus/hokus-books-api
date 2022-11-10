
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(test_config=None):
    app = Flask(__name__)

    """DB CONFIGURATION"""
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'


    db.init_app(app)
    migrate.init_app(app, db)
    from .routes import book
    from app.models.book import Book
    from app.routes.book import validate_model

    from app.routes.book import bp
    app.register_blueprint(bp)
    from app.author_routes import authors_bp
    app.register_blueprint(authors_bp)
    return app