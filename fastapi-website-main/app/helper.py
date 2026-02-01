import json
import os

DB_FILE = "database.json"


def save_data():
    with open(DB_FILE, "w") as f:
        json.dump(db, f, indent=4)
    print("Data saved to JSON.")


def load_data():
    global db
    if os.path.exists(DB_FILE):
        with open(DB_FILE, "r") as f:
            try:
                db = json.load(f)
                print("Data loaded successfully")
            except json.JSONDecodeError:
                db = []
    else:
        db = []
