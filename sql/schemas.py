from pydantic import BaseModel


class Vehiculo_detenido(BaseModel):
    nombre: str
    placas: str
    serie: str
    distrito: int
    

class Persona_bitacora(BaseModel):
    # persona_id = Column(Integer, primary_key=True)
    nombres: str
    primer_apellido: str
    segundo_apellido: str
    calle: str
    no_interior: str | None
    no_exterior: str | None
    edad: int
    # fecha_nacimiento = Column(DateTime, default=)
    colonia: str | None
    cp: int
    cve_sexo: int
    cve_gpo_criminal: int | None
    cve_pandilla: int | None
    cve_rango: int | None
    nombre_madre: str | None
    nombre_padre: str | None
    
    class Config:
        orm_mode = True