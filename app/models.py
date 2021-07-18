from sqlalchemy import Column, Float, String, Integer, Numeric, Date
from .database import Base

class coins(Base):
    __tablename__ = "coins"
    id = Column(Integer, primary_key=True, index=True)
    open_time = Column(Date)
    open = Column(Numeric)
    high = Column(Numeric)
    low = Column(Numeric)
    close = Column(Numeric)
    volume = Column(Numeric)
    close_time = Column(Date)
    coin = Column(String)
