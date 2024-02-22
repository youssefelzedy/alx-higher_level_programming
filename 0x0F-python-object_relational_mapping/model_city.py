#!/usr/bin/python3
'''
base srate model class for the project
'''

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, VARCHAR, Column, Integer, String

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
