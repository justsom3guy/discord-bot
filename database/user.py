from mongoengine import Document, StringField, IntField, BooleanField, ReferenceField
from database.monster import Monster


class User(Document):
    name = StringField(required=True, unique=True)  # Name of player
    level = IntField(default=0)  # Level of player
    xp = IntField(default=0)  # Xp of player
    floorLevel = IntField(default=0)  # Floor on which player currently is
    # Monsters founght on the highest floor player has reached
    monsterFought = IntField(default=0)
    # Status of player i.e if he is currently in fight or not
    inFight = BooleanField(default=False)
    # Highest floor player has reached till now
    floorReached = IntField(default=0)
    # Monster curently fighting if any
    monsterFighting = ReferenceField(Monster)

    def winFight(self):
        if self.xp >= 90:
            self.levelUp()
            self.update(xp=self.xp - 90)
        else:
            self.update(xp=self.xp + 10)
        self.update(
            monsterFighting=None,
            inFight=False
        )

    def loseFight(self):
        if self.xp > 5:
            self.update(xp=self.xp - 5)
        else:
            self.levelDown()
            self.update(xp=abs(self.xp-5))
        self.update(
            monsterFighting=None,
            inFight=False
        )

    def floorChange(self, number):
        if number <= self.floorReached:
            self.update(floorLevel=number)
            return f'Player reached floor {number}'
        else:
            return f'Floor not accessible'

    def foundMonster(self, monster):
        self.update(
            monsterFighting=monster,
            inFight=True
        )
        respose = f'Player has started fighting {monster.name}'
        return respose

    def giveUpFight(self):
        self.loseFight()

    def fightMonster(self):
        self.winFight()

    def levelUp(self):
        self.update(level=self.level+1)

    def levelDown(self):
        if self.level != 0:
            self.update(level=self.level-1)
