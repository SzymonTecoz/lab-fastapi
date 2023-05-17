from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}


class StudentCreateSchema(BaseModel):
    first_name: str
    last_name: str

@app.post("/items/")
async def create_item(item: StudentCreateSchema):
    return item
