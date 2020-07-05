import os

ENV = os.getenv("ENV", "development")
SECRET_KEY = os.getenv("SECRET_KEY", "MyAnnon728104@741Fortaleza/Igor")
DEBUG = os.getenv("DEBUG", True)
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "sqlite:///temp.db")
SQLALCHEMY_TRACK_MODIFICATIONS = False
