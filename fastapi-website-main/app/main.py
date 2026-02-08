from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from app.schemas import Student

from .helper import save_data, load_data
from .database import db

app = FastAPI()


load_data()


@app.get("/", response_class=HTMLResponse)
async def home():
    html_content = """
    <html>
        <head>
            <title>My Digital Profile</title>
            <style>
                body { 
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
                    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                    min-height: 100vh;
                    margin: 0;
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    padding-top: 50px;
                }
                h1 { color: #2d3436; margin-bottom: 10px; }
                p { color: #636e72; margin-bottom: 30px; }

                .profile-container {
                    display: flex;
                    flex-wrap: wrap;
                    justify-content: center;
                    gap: 20px;
                }
                .card { 
                    background: white; 
                    padding: 25px; 
                    width: 280px;
                    border-radius: 20px; 
                    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
                    transition: transform 0.3s ease;
                    text-align: left;
                    border-top: 8px solid #ff4500;
                }
                .card:hover { transform: translateY(-50px); }
                .card h2 { margin: 0 0 10px 0; color: #ff4500; font-size: 1.5em; }
                .info-item { margin: 8px 0; font-size: 0.9em; color: #2d3436; }
                .label { font-weight: bold; color: #b2bec3; text-transform: uppercase; font-size: 0.75em; }
            </style>
        </head>
        <body>
            <h1>My Digital Profile Card</h1>
            <p>Coding with FastAPI 🚀</p>
            
            <div id="data" class="profile-container"></div>

            <script>
                fetch('/students').then(r => r.json()).then(data => {
                    let container = document.getElementById('data');
                    data.forEach(s => {
                        container.innerHTML += `
                            <div class="card">
                                <h2>${s.name}</h2>
                                <div class="info-item"><span class="label">Hobby:</span> <br>${s.hobby || '保密'}</div>
                                <div class="info-item"><span class="label">Age:</span> ${s.age || '100'}</div>
                                <div class="info-item"><span class="label">Favorite Color:</span> ${s.color || 'Secret'}</div>
                                <div class="info-item"><span class="label">About Me:</span> ${s.biography || 'Secret'}</div>
                                <div class="info-item"><span class="label">Contact:</span> ${s.socials || 'Secret'}</div>
                            </div>
                        `;
                    });
                });
            </script>
        </body>
    </html>
    """
    return html_content


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
