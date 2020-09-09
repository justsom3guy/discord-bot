from mongoengine import Document, StringField, IntField, BooleanField, ReferenceField
from database.monster import Monster


class User(Document):
    name = StringField(required=True, unique=True)
    level = IntField(default=0)
    xp = IntField(default=0)
    floorLevel = IntField(default=0)
    monsterFought = IntField(default=0)
    inFight = BooleanField(default=False)
    health = IntField(default=100)
    floorReached = IntField(default=0)
    monsterFighting = ReferenceField(Monster)

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
