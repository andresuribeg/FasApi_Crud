from fastapi import FastAPI
from pydantic import BaseModel 
from typing import Optional
from database import sessionLocal

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

@app.get('/items')
def get_all_items():
    pass

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