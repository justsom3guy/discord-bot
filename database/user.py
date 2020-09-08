from mongoengine import Document, StringField, IntField


class User(Document):
    name = StringField(required=True, unique=True)
    player_level = IntField(default=0)
    xp = IntField(default=0)
    floor_level = IntField(default=0)
