from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal, PeticionDB  # Importamos el modelo
from datetime import datetime

app = FastAPI()

# Modelo de datos para la petición
class Peticion(BaseModel):
    descripcion: str

# Modelo de respuesta
class PeticionResponse(BaseModel):
    id: int
    descripcion: str
    tipo: str
    estado: str
    fecha_creacion: datetime

    class Config:
        from_attributes = True

# Dependencia para la BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Función simple para clasificar peticiones
def clasificar_peticion(texto: str) -> str:
    texto = texto.lower()
    if "permiso" in texto:
        return "Solicitud de permiso"
    elif "vacaciones" in texto:
        return "Solicitud de vacaciones"
    elif "baja" in texto:
        return "Solicitud de sustitución por baja"
    return "Desconocido"

# Endpoint para crear una petición
@app.post("/peticiones/", response_model=PeticionResponse)
async def crear_peticion(peticion: Peticion, db: Session = Depends(get_db)):
    tipo = clasificar_peticion(peticion.descripcion)
    
    # Crear nueva petición en la BD
    nueva_peticion = PeticionDB(
        descripcion=peticion.descripcion,
        tipo=tipo,
        estado="Pendiente"
    )
    db.add(nueva_peticion)
    db.commit()
    db.refresh(nueva_peticion)
    
    return nueva_peticion

# Endpoint para obtener todas las peticiones
@app.get("/peticiones/", response_model=list[PeticionResponse])
async def listar_peticiones(db: Session = Depends(get_db)):
    return db.query(PeticionDB).all()