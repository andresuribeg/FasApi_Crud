from fastapi import FastAPI
from pydantic import BaseModel 
from typing import Optional, List
from database import sessionLocal
import models

app=FastAPI()

class Item(BaseModel):
    id:int
    nombre:str
    descripcion:str
    precio:int
    en_oferta:bool

    class Config:
        orm_mode=True

db=sessionLocal()

@app.get('/items', response_model=List[Item],status_code=200)
def get_all_items():
    items=db.query(models.Item).all()

    return items

@app.get('/item/{item_id}')
def get_an_item(item_id:int):
    pass

@app.post('/items')
def create_an_item():
    pass

@app.put('/item/{item_id}')
def update_an_item(item_id:int):
    pass

@app.delete ('/item/{item_id}')
def delete_item(item_id:int):
    pass