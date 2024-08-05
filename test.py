from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from sql.databases.world import SessionLocal, engine
from sql.models import world as models
from sql.schemas import world as schemas


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/city/{city_name}", response_model=schemas.City)
def read_city(city_name: str, db: Session = Depends(get_db)):
    city_name = city_name.title()
    return db.query(models.City).filter(models.City.name == city_name).first()

@app.get("/country/{country_code}")
def read_country(country_code: str, db: Session = Depends(get_db)):
    country_code = country_code.upper()
    return db.query(models.Country).filter(models.Country.code == country_code).first()