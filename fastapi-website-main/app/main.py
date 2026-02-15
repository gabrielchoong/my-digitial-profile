from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.schemas import Student

from .helper import save_data, load_data
from .database import db

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/templates"), name="static")
app.mount("/assets", StaticFiles(directory="app/assets"), name="assets")


load_data()


@app.get("/", response_class=HTMLResponse)
async def home():
    with open("app/templates/index.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content)


@app.get("/students")
async def get_students():
    return db


@app.post("/add-student")
async def add_student(student: Student):
    db.append(student.model_dump())
    return {"message": f"Added {student.name}'s profile!"}


@app.delete("/delete-student/{name}")
async def delete_student(name: str):
    global db

    student_found = False

    for i in range(len(db) - 1, -1, -1):
        if db[i]["name"] == name:
            del db[i]
            student_found = True
            break

        if student_found:
            return {"message": f"Deleted {name}'s profile successfully!"}
        else:
            return {"message": f"Student {name} not found!"}


@app.post("/save-everything")
async def save_everything():
    save_data()
    return {"message": "All data has been saved to disk!"}
