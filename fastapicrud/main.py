from typing import List
from fastapi import FastAPI
from fastapi.params import Depends
import models,schemas
from database import SessionLocal,engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get('/getusers/',response_model=List[schemas.User])
def show_users(db:Session=Depends(get_db)):
    obj = db.query(models.User).all()
    return obj

@app.post('/createtodo/',response_model=schemas.User)
def create_users(item:schemas.User,db:Session=Depends(get_db)):
    obj = models.User(id=item.id,username = item.username,nombre=item.nombre,rol=item.rol,estado=item.estado)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

@app.put('/updatetodo/{todo_id}',response_model=schemas.User)
def update_users(todo_id:int,item:schemas.UserUpdate,db:Session=Depends(get_db)):
    obj = db.query(models.User).filter_by(id=todo_id).first()
    obj.nombre=item.nombre
    db.commit()
    db.refresh(obj)
    return obj

@app.delete('/deletetodo/{todo_id}',response_model=schemas.User)
def delete_users(todo_id:int,db:Session=Depends(get_db)):
    obj = db.query(models.User).filter_by(id=todo_id).first()
    db.delete(obj)
    db.commit()
    return obj