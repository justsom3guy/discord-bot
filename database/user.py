from mongoengine import Document, StringField, IntField


class User(Document):
    name = StringField(required=True, unique=True)
    level = IntField(required=True)
