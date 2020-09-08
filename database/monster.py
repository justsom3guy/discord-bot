from mongoengine import Document, StringField, IntField


class Monster(Document):
    name = StringField(required=True, unique=True)
