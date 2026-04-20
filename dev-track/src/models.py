from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DB_URL

Base = declarative_base()
engine = create_engine(DB_URL)
SessionLocal = sessionmaker(bind=engine)


class Lv(Base):
    __tablename__ = "leaves"

    id = Column(Integer, primary_key=True)
    n = Column(String(50))
    d = Column(String(20))
    ed = Column(String(20))
    s = Column(String(10), default="pending")
    t = Column(String(20))
    r = Column(String(200))
    dept = Column(String(50))
    mgr = Column(String(50))
    cr = Column(DateTime)


class Emp(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    n = Column(String(50))
    e = Column(String(100))
    dept = Column(String(50))
    mgr_id = Column(Integer)
    bal = Column(Integer, default=15)
    p = Column(String(20))


class Dept(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True)
    n = Column(String(50))
    hd = Column(Integer)
    loc = Column(String(50))


Base.metadata.create_all(engine)
