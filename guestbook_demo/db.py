from datetime import datetime
import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.schema import Column
from sqlalchemy.types import DateTime, Integer, Unicode

engine = create_engine(os.environ.get('HEROKU_POSTGRESQL_JADE_URL', 'postgresql:///guestbook_demo'))
session = scoped_session(sessionmaker(bind=engine, autoflush=False))

Base = declarative_base(bind=engine)


### Yonder tables

class GuestbookEntry(Base):
    __tablename__ = 'guestbook_entries'

    id = Column(Integer, primary_key=True, nullable=False)
    timestamp = Column(DateTime, nullable=False, index=True)
    name = Column(Unicode, nullable=False)
    message = Column(Unicode, nullable=False)

    def __init__(self, **kwargs):
        kwargs.setdefault('timestamp', datetime.utcnow())

        super(GuestbookEntry, self).__init__(**kwargs)
