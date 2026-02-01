from pydantic import BaseModel

class Student(BaseModel):
    name: str
    hobby: str
    age: str
    color: str