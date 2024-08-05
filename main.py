from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from sql.schemas import detenidos as schemas
from sql.models import detenidos as models
from sql.databases.detenidos import SessionLocal, engine
from sql.models import detenidos


detenidos.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/detenido/{id}", response_model=schemas.Persona)
def read_user(id: int, db: Session = Depends(get_db)):
   return db.query(models.Persona).filter(models.Persona.persona_id == id).first()


@app.get("/vehiculo/placa/{placa}", response_model=schemas.Vehiculo)
def read_vehiculo(placa: str, db: Session = Depends(get_db)):
    return db.query(models.Vehiculos_detenidos).filter(models.Vehiculos_detenidos.placa == placa).first()


@app.get("/vehiculo/serie/{serie}", response_model=schemas.Vehiculo)
def read_vehiculo(serie: str, db: Session = Depends(get_db)):
    return db.query(models.Vehiculos_detenidos).filter(models.Vehiculos_detenidos.serie == serie).first()