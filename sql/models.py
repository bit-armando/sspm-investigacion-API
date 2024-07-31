from sqlalchemy import Column, Integer, String, DateTime
# from sqlalchemy.orm import relationship

from .database import Base


class Vehiculos_detenidos(Base):
    __tablename__ = 'VEHICULOS_DET'
    
    vehiculo_id = Column(Integer, primary_key=True)
    persona_id = Column(Integer)
    nombre = Column('nombre_quienasegura', String(200))
    placas = Column('numero_placas', String(30))
    serie = Column('numero_serie', String(20))
    distrito = Column('cve_distrito', Integer)
    


class Persona_bitacora(Base):
    __tablename__ = 'PERSONAS_MST_BIT'
    
    persona_id = Column(Integer, primary_key=True)
    nombres = Column(String(50))
    primer_apellido = Column(String(50))
    segundo_apellido = Column(String(50))
    calle = Column(String(60))
    no_interior = Column(String(20))
    no_exterior = Column(String(20))
    edad = Column(Integer)
    # fecha_nacimiento = Column(DateTime, default=)
    colonia = Column(String(60))
    cp = Column(Integer)
    cve_sexo = Column(Integer)
    cve_gpo_criminal = Column(Integer)
    cve_pandilla = Column(Integer)
    cve_rango = Column(Integer)
    nombre_madre = Column(String(150))
    nombre_padre = Column(String(150))

    