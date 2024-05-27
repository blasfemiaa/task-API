from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
#python -m uvicorn main:app --reload


class lista(BaseModel):
    id: int
    title: str
    description: str
    status: str
    due_date: str
    
tasks = []

@app.post("/task/create")
async def createtask(task: lista):
    for x in tasks:
        if x.id == task.id:
            return "ya existe esta tarea"
    tasks.append(task)
    return "tarea creada"

@app.get("/task/{id}")
async def looktask(id: int):
    for x in tasks:
       if x.id == id:
           return x
    return "no existe la tarea"

@app.put("/task/update/{id}")
async def puttask(id: int, newlist: lista):
    for z, x in enumerate(tasks):
        if x.id == id:
            tasks[z] = newlist
            return  tasks[z]
        
    return "no existe la tarea"

@app.delete("/task/delete/{id}")
async def deletetask(id: int):
    for x in tasks:
        if x.id == id:
            tasks.remove(x)
            return "tarea eliminada"
    return "no se puede eliminar esta tarea"
            
            