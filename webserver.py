import json
from pathlib import Path
from typing import List

from fastapi import FastAPI

app = FastAPI()
p = Path('db.json')
with p.open('r') as file:
    file_data = file.read()
    expenses: List = json.loads(file_data) if file_data else []


@app.get("/")
async def root():
    return {"message": "Hello Anton"}


@app.get("/list")
async def list_of_expenses():
    result = []
    for index, expense in enumerate(expenses):
        result.append({f'{index + 1}': expense})
    return {"expenses": result}
