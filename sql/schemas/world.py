from pydantic import BaseModel
from typing import Optional

        
class Country(BaseModel):
    code: str
    name: str
    continent: str
    region: str
    surfacearea: int
    indepyear: int
    population: int
    lifeexpectancy: float
    gnp: int
    gnpold: int
    localname: str
    governmentform: str
    headofstate: str
    capital: int
    code2: str
    
    class Config:
        from_attributes = True
        

class City(BaseModel):
    id: int
    name: str
    countrycode: str
    district: str
    population: int
    
    country: Optional[Country]
    
    class Config:
        from_attributes = True