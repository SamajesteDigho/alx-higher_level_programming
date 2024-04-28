#!/usr/bin/python3
"""
    The module file for the Exo 14
    Here we define the rules
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3],
    ), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).all()

    for x in cities:
        state = session.query(State).filter(State.id == x.state_id).first()
        print("{}: ({}) {}".format(state.name, x.id, x.name))
