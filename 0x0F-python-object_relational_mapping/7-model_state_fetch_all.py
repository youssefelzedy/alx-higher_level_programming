#!/usr/bin/python3
'''
7-model_state_fetch_all.py:
script that lists all State objects from the database hbtn_0e_6_usa
Usage: ./7-model_state_fetch_all.py <mysql username> <mysql password>
<database name>
'''

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, VARCHAR, Column, Integer, String
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    session.close()
