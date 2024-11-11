# TODO решите задачу
import json

def task() -> float:
    file = "input.json"
    with open(file) as file:
        json_data = json.load(file)
    total = sum([item["score"] * item["weight"] for item in json_data])
    return round(total, 3)

print(task())
