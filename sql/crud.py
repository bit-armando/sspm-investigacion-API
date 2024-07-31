from sqlalchemy.orm import Session

from . import models


def get_vehiculo_id(db: Session, id: int):
    return db.query(models.Vehiculos_detenidos).filter(models.Vehiculos_detenidos.vehiculo_id == id).first()


def get_user_id(db: Session, id: int):
    return db.query(models.Persona_bitacora).filter(models.Persona_bitacora.persona_id == id).first()


def get_detenido_by_colonia(db: Session, col: str):
    return db.query(models.Persona_bitacora).filter(models.Persona_bitacora.colonia == col).first()