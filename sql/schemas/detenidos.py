from pydantic import BaseModel
from datetime import datetime


class Vehiculo(BaseModel):
    nombre: str
    placa: str
    serie: str
    distrito: int
    

class Foto(BaseModel):
    persona_id: int
    img: str
    

class Persona(BaseModel):
    nombres: str
    primer_apellido: str
    segundo_apellido: str
    calle: str
    no_interior: str | None
    no_exterior: str | None
    fecha_nacimiento: datetime
    colonia: str | None
    cp: int
    nombre_madre: str | None
    nombre_padre: str | None
    # foto: Foto | None
    
    class Config:
        from_atributes = True


# class PersonaResponse(BaseModel):
#     nombres: str
#     primer_apellido: str
#     segundo_apellido: str
#     calle: str
#     no_interior: str | None
#     no_exterior: str | None
#     fecha_nacimiento: datetime
#     colonia: str | None
#     cp: int
#     nombre_madre: str | None
#     nombre_padre: str | None
#     foto: str | None
    
#     @classmethod
#     def from_persona(cls, persona: Persona):
#         return cls(
#             nombres=persona.nombres,
#             primer_apellido=persona.primer_apellido,
#             segundo_apellido=persona.segundo_apellido,
#             calle=persona.calle,
#             no_interior=persona.no_interior,
#             no_exterior=persona.no_exterior,
#             fecha_nacimiento=persona.fecha_nacimiento,
#             colonia=persona.colonia,
#             cp=persona.cp,
#             nombre_madre=persona.nombre_madre,
#             nombre_padre=persona.nombre_padre,
#             foto=persona.foto.img
#         )