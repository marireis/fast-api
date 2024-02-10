from fastapi import FastAPI, HTTPException
from typing import List
from models import User, Role
from uuid import UUID

app = FastAPI()

db: List[User] = [
    User(id = UUID("1ce2794e-485d-429d-b0a0-2caf2d73e3ae"),
        first_name="Marina", 
        last_name="Reis",
        email="marinareis@gmail.com", 
        role=[Role.role_1]
    ),

    User(id = UUID("f689366e-e3bf-485b-a7fc-1fd66345c969"),
        first_name="Joao", 
        last_name="Lacerda",
        email="jj@gmail.com", 
        role=[Role.role_2]
    ),

    User(id = UUID("904c70df-a744-4f23-a1bd-35a25e87b146"),
        first_name="Camila", 
        last_name="Silva",
        email="email@gmail.com", 
        role=[Role.role_3]
    ),
]

@app.get("/")
async def root():
    return{"message": "Olá WoMakers"}

@app.get("/api/users")
async def get_users():
    return db

@app.get("/api/users/{id}")
async def get_user(id: UUID):
    for user in db:
        if user.id == id:
            return user
        return{"message": "Usuario não encontrado"}
    
@app.post("/api/users")
async def add_user(user: User):
    db.append(user)
    return{"id": user.id}

@app.delete("/api/users/{id}")
async def remove_user(id:UUID):
    for user in db:
        if user.id == id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code = 404,
        details = f"Usuario com o id {id} não encontrado!"
    )    
    