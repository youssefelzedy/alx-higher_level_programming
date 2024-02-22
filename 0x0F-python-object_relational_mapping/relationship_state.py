#!/usr/bin/python3
'''
base srate model class for the project
'''

from sqlalchemy.orm import declarative_base, sessionmaker, relationship
from sqlalchemy import create_engine, VARCHAR, Column, Integer, String

Base = declarative_base()


class State(Base):
    '''
    State class
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
