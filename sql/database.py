from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import oracledb


oracledb.init_oracle_client()
cadena_conexion = "oracle+oracledb://DETENIDOS:XGtlDoGfHz9HdkSzrp5X@10.236.21.137/?service_name=sspm3701.juarez.gob.mx"
# cadena_conexion = "mysql+pymysql://Armando:Rosmacias1500@25.59.114.104:3306/world"
engine = create_engine(cadena_conexion)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()