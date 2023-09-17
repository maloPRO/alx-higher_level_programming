#!/usr/bin/python3

"""
Lists all cities
"""

from model_state import Base, State
from model_city import Base, City
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

    cities = session.query(City, State)
    cities = cities.join(State, City.state_id == State.id)
    cities = cities.all()

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
