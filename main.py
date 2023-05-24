from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from functools import lru_cache

class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str
    class Config(BaseModel):
        schema_extra = {
            "Student 1":{
                "first_name": "Andrzej",
                "last_name": "Kowalski"
            }
        }
app = FastAPI()

#class StudentUpdateSchema(BaseModel):
students =[]

@app.get("/students/{id}")
async def root(id:int):
    if len(students)<= id:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"student": students[id]}

async def read_item(id: int):
    return {"item_id": id}


@app.post("/students")
async def create_item(item: StudentCreateSchema):
    students.append(item)
    return item
