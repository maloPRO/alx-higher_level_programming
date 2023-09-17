#!/usr/bin/python3

"""
Lists all states
"""

from model_state import Base, State
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'
            .format(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    inpt = sys.argv[4]

    states = session.query(State).filter(State.name == inpt).all()

    if states:
        print(f"{states[0].id}")
    else:
        print("Not found")
