from database import Base
from sqlalchemy import String, Boolean, Integer, Column, Text

class Item(Base):
    __tablename__='items'
    id=Column(Integer, primary_key=True)
    nombre=Column(String(255), nullable=False, unique=True)
    descripcion=Column(Text)
    precio=Column(Integer, nullable=False)
    en_oferta=Column(Boolean, default=False)

    def __repr__(self):
        return f"<Item nombre={self.nombre} precio={self.precio}>"