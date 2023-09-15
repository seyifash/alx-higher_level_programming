#!/usr/bin/python3
"""script that lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa
"""
import sys
from sqlalchemy import (create_engine)
from model_stae import Base, State
from sqlalchemy.orm import sessionmaker

if __name == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).order_by
    (State.id).first()

    if states is not none:
        print("{}: {}".format(states.id, states.name))
    else:
        print("Nothing")
