from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sql import crud, models, schemas
from sql.database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# @app.get("/city/{city_name}", response_model=schemas.City)
# def read_user(city_name: str, db: Session = Depends(get_db)):
#     db_user = crud.get_city(db,city_name=city_name)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="City not found")
#     return db_user

@app.get("/detenido/{id}", response_model=schemas.Persona_bitacora)
def read_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user_id(db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Detenido no encontrado")
    return db_user


@app.get("/detenidos/{colonia}", response_model=schemas.Persona_bitacora)
def get_by_colonia(colonia: str, db: Session = Depends(get_db)):
    db_user = crud.get_detenido_by_colonia(db,col=colonia)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Detenido no encontrado")
    return db_user


@app.get("/vehiculo/{id}", response_model=schemas.Vehiculo_detenido)
def read_user(id: int, db: Session = Depends(get_db)):
    db_user = crud.get_vehiculo_id(db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Detenido no encontrado")
    return db_user