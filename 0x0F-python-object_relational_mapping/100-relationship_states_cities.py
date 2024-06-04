#!/usr/bin/python3
"""
    The module file for the Exo 14
    Here we define the rules
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City, Base as CBase
from relationship_state import State, Base as SBase
from sqlalchemy.orm import declarative_base

Base = declarative_base()

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3],
    ), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(bind=engine)

    state = State(name="California")
    city = City(name="San Francisco")
    city.state_id = state


    session.add(state)
    # session.add(city)

    session.commit()
