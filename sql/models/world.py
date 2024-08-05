from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from sql.databases.world import Base


class Country(Base):
    __tablename__ = 'country'
    
    code = Column(String(3), primary_key=True)
    name = Column(String(52))
    continent = Column(String(13))
    region = Column(String(26))
    surfacearea = Column(Integer)
    indepyear = Column(Integer)
    population = Column(Integer)
    lifeexpectancy = Column(Float)
    gnp = Column(Integer)
    gnpold = Column(Integer)
    localname = Column(String(45))
    governmentform = Column(String(45))
    headofstate = Column(String(60))
    capital = Column(Integer)
    code2 = Column(String(2))
    
    # cities = relationship('City', back_populates='country')
    
    
class City(Base):
    __tablename__ = 'city'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    countrycode = Column(String(3), ForeignKey('country.code'))
    district = Column(String(50))
    population = Column(Integer)
    
    country = relationship('Country')