from fastapi import FastAPI,status,HTTPException
from pydantic import BaseModel
from typing import Optional,List
from database import SessionLocal
import models

app=FastAPI()

class Item(BaseModel): #serializer
    id:int
    nombre:str
    descripcion:str
    Precio:int
    en_oferta:bool

    class Config:
        orm_mode=True


db=SessionLocal()

@app.get('/items',response_model=List[Item],status_code=200)
def get_all_items():
    items=db.query(models.Item).all()

    return items

@app.get('/item/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
def get_an_item(item_id:int):
    item=db.query(models.Item).filter(models.Item.id==item_id).first()
    return item

@app.post('/items',response_model=Item,
        status_code=status.HTTP_201_CREATED)
def create_an_item(item:Item):
    db_item=db.query(models.Item).filter(models.Item.nombre==item.nombre).first()

    if db_item is not None:
        raise HTTPException(status_code=400,detail="Item already exists")



    new_item=models.Item(
        nombre=item.nombre,
        Precio=item.Precio,
        descripcion=item.descripcion,
        en_oferta=item.en_oferta
    )


    

    db.add(new_item)
    db.commit()

    return new_item

@app.put('/item/{item_id}',response_model=Item,status_code=status.HTTP_200_OK)
def update_an_item(item_id:int,item:Item):
    item_to_update=db.query(models.Item).filter(models.Item.id==item_id).first()
    item_to_update.nombre=item.nombre
    item_to_update.Precio=item.Precio
    item_to_update.descripcion=item.descripcion
    item_to_update.en_oferta=item.en_oferta

    db.commit()

    return item_to_update

@app.delete('/item/{item_id}')
def delete_item(item_id:int):
    item_to_delete=db.query(models.Item).filter(models.Item.id==item_id).first()

    if item_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Registro no encontrado")
    
    db.delete(item_to_delete)
    db.commit()

    return item_to_delete
