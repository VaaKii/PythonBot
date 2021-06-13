from sqlalchemy import create_engine, Column,Text,Integer, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists

Base = declarative_base()
engine = create_engine("postgresql://vlad:vlad@db/server")
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer,primary_key=True)
    experience = Column(Integer)
    money = Column(Integer)
    level = Column(Integer)

    def __repr__(self):
        return f"<User(id = {self.id}, experience={self.experience}, money={self.money},level={self.level})>"
    
class Private(Base):
    __tablename__ = 'privates'

    channel_id = Column(Integer,primary_key=True)
    count_members = Column(Integer)

    def __repr__(self):
        return f"<Private(channel_id = {self.channel_id}, count_members = {self.count_members})>"

class Muted(Base):
    __tablename__ = 'muted'

    id = Column(Integer,primary_key=True)
    timewarn = Column(TIMESTAMP)

    def __repr__(self):
        return f"<Warned(id = {self.id}, timewarn = {self.timewarn})>"

def get_user(id: int):
    return session.query(User).filter_by(id=id).first()

def exists_user(id:int):
    return session.query(exists().where(User.id == id)).scalar()

def add_user(user: User):
    session.add(user)
    session.commit()

def all():
    return session.query(User).all()

def delete_user(user: User):
    session.delete(user)

def get_private(id: int):
    return session.query(Private).filter_by(channel_id=id).first()

def add_private(private: Private):
    session.add(private)
    session.commit()

def add_mute(mute: Muted):
    session.add(mute)
    session.commit()

def get_all(table):
    return session.query(table).all()

def delete_mute(mute: Muted):
    session.delete(mute)
    session.commit()
    