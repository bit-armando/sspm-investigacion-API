from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


cadena_conexion = "mysql+pymysql://Armando:Rosmacias1500@25.59.114.104:3306/world"
engine = create_engine(cadena_conexion)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()