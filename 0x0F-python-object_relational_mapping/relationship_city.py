#!/usr/bin/python3
'''
base srate model class for the project
'''

from relationship_state import Base, State
from sqlalchemy import Column, Integer, VARCHAR, ForeignKey

Base = declarative_base()


class City(Base):
    '''
    cities class
    '''
    __tablename__ = 'cities'

    id = Column('id', Integer, primary_key=True)
    name = Column('name', VARCHAR(128), nullable=False)
    state_id = Column('state_id',   Integer,
                      ForeignKey('State.id'), nullable=False)
