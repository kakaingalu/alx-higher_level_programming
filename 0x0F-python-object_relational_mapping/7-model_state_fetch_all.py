#!/usr/bin/python3
"""
a script that lists all State objects from the\
        database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    access the datbase and get states
    """
    db = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3])

    engine = create_engine(db)

    Session = sessionmaker(bind=engine)
   
    session = Session()

    states = session.query(State).order_by(State.id)

    for state in states:
        print("{0}:{1}".format(state.id, state.name))
