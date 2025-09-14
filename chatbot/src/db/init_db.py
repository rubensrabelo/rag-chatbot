from sqlmodel import create_engine, Session

from config import URL_DATABASE

engine = create_engine(URL_DATABASE)


def get_session():
    return Session(engine)
