from fastapi import Depends, APIRouter
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

import base64

from sql.schemas import detenidos as schemas
from sql.models import detenidos as models
from depends.database import get_db

router = APIRouter(
    prefix='/detenido',
    tags=['detenido']
)


@router.get("/{id}", response_model=schemas.Persona)
def read_user(id: int, db: Session = Depends(get_db)):
    persona = db.query(models.Persona).filter(models.Persona.persona_id == id).first()
    return persona


# @router.get("/vehiculo/placa/{placa}", response_model=schemas.Vehiculo)
# def read_vehiculo(placa: str, db: Session = Depends(get_db)):
#     return db.query(models.Vehiculos_detenidos).filter(models.Vehiculos_detenidos.placa == placa).first()


# @router.get("/vehiculo/serie/{serie}", response_model=schemas.Vehiculo)
# def read_vehiculo(serie: str, db: Session = Depends(get_db)):
#     return db.query(models.Vehiculos_detenidos).filter(models.Vehiculos_detenidos.serie == serie).first()


@router.get("/foto/{id}")
def read_foto(id: int, db: Session = Depends(get_db)):
    image =  db.query(models.Foto).filter(models.Foto.persona_id == id).first()
    encodingString = base64.b64encode(image.img).decode('utf-8')
    # return {"img": str(type(encodingString))}
    html_content = """
    <html>
        <body>
            <img src="data:image/png;base64,{}">
        </body>
    </html>
    """
    return HTMLResponse(content=html_content.format(encodingString))


# @router.get("/delitos/{id}")
# def read_delitos(id: int, db: Session = Depends(get_db)):
#     return db.query(models.DelitoCometido).filter(models.DelitoCometido.persona_id == id).all()