from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

SQLALCHEMY_DATABASE_URL = "sqlite:///./peticiones.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelo de datos para las peticiones
class PeticionDB(Base):
    __tablename__ = "peticiones"

    id = Column(Integer, primary_key=True, index=True)
    descripcion = Column(String, index=True)
    tipo = Column(String)
    estado = Column(String, default="Pendiente")
    fecha_creacion = Column(DateTime, default=datetime.now(datetime.timezone.utc))

# Crear las tablas
Base.metadata.create_all(bind=engine)