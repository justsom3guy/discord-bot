from mongoengine import Document, StringField, IntField, BooleanField, ReferenceField
from database.monster import Monster


class User(Document):
    name = StringField(required=True, unique=True)
    player_level = IntField(default=0)
    xp = IntField(default=0)
    floor_level = IntField(default=0)
    monster_fought = IntField(default=0)
    infight = BooleanField(default=False)
    health = IntField(default=100)
    floorReached = IntField(default=0)
    monster_fighting = ReferenceField(Monster)

    def winFight(self):
        pass

    def loseFight(self):
        pass

    def floorChange(self):
        pass

    def foundMonster(self):
        pass

    def giveUpFight(self):
        pass

    def fightMOnster(self, monster):
        pass
