#!/usr/bin/python3
"""
    The module file for the Exo 8
    Here we define the rules
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(State).first()

    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
