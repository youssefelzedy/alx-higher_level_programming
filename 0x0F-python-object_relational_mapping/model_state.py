#!/usr/bin/python3


'''
7-model_state_fetch_all.py:
script that lists all State objects from the database hbtn_0e_6_usa
Usage: ./7-model_state_fetch_all.py <mysql username> <mysql password>
<database name>
'''

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from model_state import Base
from sqlalchemy import create_engine, VARCHAR, Column, Integer, String
import sys

Base = declarative_base()

class State(Base):
    '''
    State class
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
