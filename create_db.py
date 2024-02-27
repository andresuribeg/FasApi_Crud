from database import Base, engine
from models import Item

print ("Creando base de datos.......")

Base.metadata.create_all(engine)