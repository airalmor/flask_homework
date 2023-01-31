import atexit
from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

PG_DSN = 'postgresql://app:1234@127.0.0.1:5433/flask_hw_db'

engine = create_engine(PG_DSN)
Base = declarative_base(bind=engine)



class AdvertModel(Base):
    __tablename__ = 'adverts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    advert_title = Column(String(50), nullable=False)
    advert_text = Column(String, nullable=False)
    creation_time = Column(DateTime, server_default=func.now())
    owner_name = Column(String(50), nullable=False)


Base.metadata.create_all()
Session = sessionmaker(bind=engine)

atexit.register(engine.dispose)
