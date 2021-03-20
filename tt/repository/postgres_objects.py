from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TimeEntry(Base):
    __tablename__ = "time_entry"

    id = Column(Integer, primary_key=True)

    code = Column(String(36), nullable=False)
    project = Column(String(255))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    description = Column(String(512))
