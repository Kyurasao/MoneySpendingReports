import atexit
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import List, Union, Optional

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


@atexit.register
def on_exit(exception: Optional[str] = None, exit_code: Optional[int] = None):
    # Perform cleanup or finalization tasks here
    print("Exiting...")
    p = Path('db.json')
    with p.open('w+') as f:
        json.dump(expenses, f)  # Raise SystemExit to trigger the exit event
    raise SystemExit(exit_code)


class Item(BaseModel):
    time: Union[str, datetime]
    payer: str
    amount: str
    category: str
    method: str


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
    for index, expense_ in enumerate(expenses):
        result.append({f'{index + 1}': expense_})
    return {"expenses": result}


@app.get("/expense/{item_id}")
async def expense(item_id: int):
    return {"item_id": expenses[int(item_id) - 1]} if item_id in range(1, len(expenses) + 1) else {
        "error": f"id [{item_id}] out of range [1:{len(expenses)}]"}


@app.post("/create")
async def create_item(item: Item):
    # преобраховать данные из item в формат данных из db.json
    # добавить преобразованные данные в expenses
    details = {'payer': item.payer, 'amount': item.amount, 'category': item.category,
               'method': item.method}
    time_value = datetime.now() if item.time == 'now' else item.time
    expenses.append({time_value: details})
    return item


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
    sys.exit(0)
