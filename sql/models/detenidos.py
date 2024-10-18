from sqlalchemy import Column, Integer, String, DateTime, LargeBinary, ForeignKey
from sqlalchemy.orm import relationship

from sql.databases.detenidos import Base
    
class Usuario(Base):
    __tablename__ = 'USUARIOS_API'

    nombres = Column(String)
    primer_apellido = Column(String)
    username = Column(String, primary_key=True)
    password = Column(String)
    estatus = Column(Integer)
    token = Column(String)


class Persona(Base):
    __tablename__ = 'PERSONAS_MST'
    
    persona_id = Column(Integer, primary_key=True)
    nombres = Column(String(50))
    primer_apellido = Column(String(50))
    segundo_apellido = Column(String(50))
    calle = Column(String(60))
    no_interior = Column(String(20))
    no_exterior = Column(String(20))
    fecha_nacimiento = Column(DateTime)
    colonia = Column(String(60))
    cp = Column(Integer)
    cve_sexo = Column(Integer)
    nombre_madre = Column(String(150))
    nombre_padre = Column(String(150))
    

class Foto(Base):
    __tablename__ = 'FOTOS_BLOBS_DVD'
    
    foto_id = Column('FOTO_ID', Integer, primary_key=True)
    persona_id = Column(Integer)
    img = Column('FOTO_IMAG', LargeBinary)
        

class DelitoCometido(Base):
    __tablename__ = 'DELITOS_COMETIDOS'
    
    id = Column('DELITO_COMETIDO_ID', Integer, primary_key=True)
    persona_id = Column('PERSONA_ID', Integer, ForeignKey('PERSONAS_MST.persona_id'))
    descripcion = Column('DESCRIPCION_HECHOS', String(1500))
    fecha = Column('FEHORA_REGISTRO', DateTime)
    
    persona = relationship('Persona')
    

class Vehiculos_detenidos(Base):
    __tablename__ = 'VEHICULOS_DET'
    
    vehiculo_id = Column(Integer, primary_key=True)
    persona_id = Column(Integer)
    nombre = Column('nombre_quienasegura', String(200))
    placa = Column('numero_placas', String(30))
    serie = Column('numero_serie', String(20))
    distrito = Column('cve_distrito', Integer)