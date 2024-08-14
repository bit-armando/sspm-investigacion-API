from pydantic import BaseModel
from datetime import datetime


class Vehiculo(BaseModel):
    nombre: str
    placa: str
    serie: str
    distrito: int
    

class Foto(BaseModel):
    persona_id: int
    img: bytes
    

class Persona(BaseModel):
    nombres: str
    primer_apellido: str
    segundo_apellido: str
    # foto: Foto
    calle: str
    no_interior: str | None
    no_exterior: str | None
    fecha_nacimiento: datetime
    colonia: str | None
    cp: int
    nombre_madre: str | None
    nombre_padre: str | None
    
    @property
    def fecha_nacimiento(self) -> str:
        return self.fecha_nacimiento.strftime('%Y-%m-%d')
    
    class Config:
        orm_mode = True