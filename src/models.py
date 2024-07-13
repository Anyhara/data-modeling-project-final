import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Apoderado(Base):
    __tablename__ = 'apoderado'
    id = Column(Integer, primary_key=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String(120), nullable=False)
    correo_electronico = Column(String(120), unique=True, nullable=False)
    contrasena = Column(String(80), nullable=False)
    esta_activo = Column(Boolean, nullable=False, default=False)
    telefono = Column(String(20), nullable=True)
    direccion = Column(String(250), nullable=True)
    
class Profesor(Base):
    __tablename__ = 'profesor'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False)
    apellido = Column(String(120), nullable=False)
    correo_electronico = Column(String(120), unique=True, nullable=False)
    contrasena = Column(String(80), nullable=False)
    esta_activo = Column(Boolean, nullable=False, default=False)
    titulo = Column(String(120), nullable=True)
    especializacion = Column(String(120), nullable=True)
   
class Asignatura(Base):
    __tablename__ = 'asignatura'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False)
    id_profesor = Column(Integer, ForeignKey('profesor.id'))
    
class Alumno(Base):
    __tablename__ = 'alumno'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(120), nullable=False)
    apellido = Column(String(120), nullable=False)
    id_apoderado = Column(Integer, ForeignKey('apoderado.id'))
    id_asignatura = Column(Integer, ForeignKey('asignatura.id'))
    esta_activo = Column(Boolean, nullable=False, default=False)
   
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
