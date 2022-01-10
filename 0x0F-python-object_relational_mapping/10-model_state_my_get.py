#!/usr/bin/python3
'''
prints the State object with the name passed
as argument from the database hbtn_0e_6_usa
'''
import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(name=argv[4]).first()
    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
