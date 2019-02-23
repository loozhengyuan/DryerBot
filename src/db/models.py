from peewee import *


db = SqliteDatabase('dryer.db')

class BaseModel(Model):
    uuid = UUIDField(default=uuid.uuid4)
    class Meta:
        database = db


class User(BaseModel):
    username = CharField(unique=True)
    password = CharField()
    email = CharField()
    join_date = DateTimeField()


class Message(BaseModel):
    user = ForeignKeyField(User, backref='messages')
    content = TextField()
    pub_date = DateTimeField()


def create_tables():
    with db:
        db.create_tables([User, Message])