from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.sql import func

Base = declarative_base()


class GardenBed(Base):
    __tablename__ = 'bed'
    id = Column(Integer, primary_key=True)
    size = Column(Integer)
    life_factor = Column(Integer)
    garden_id = Column(Integer, ForeignKey("garden.id"))

    def __repr__(self):
        return f"<GardenBed(size='{self.size}', life_factor='{self.life_factor}', garden_id='{self.garden_id}')>"


class Garden(Base):
    __tablename__ = 'garden'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"<Garden(name='{self.name}')>"


class Plant(Base):
    __tablename__ = 'plant'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    stage = Column(Integer)
    bed_id = Column(Integer, ForeignKey("bed.id"))

    def __repr__(self):
        return f"<Plant(name='{self.name}', stage='{self.stage}', bed_id='{self.bed}')>"
