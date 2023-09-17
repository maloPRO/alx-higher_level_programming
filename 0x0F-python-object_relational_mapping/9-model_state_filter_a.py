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

    a_states = session.query(State).order_by(State.id)\
        .filter(State.name.like('%a%')).all()

    for state in a_states:
        print(f"{state.id}: {state.name}")
