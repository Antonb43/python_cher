import json

def load_notes(filename="notes.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  

def save_notes(notes, filename="notes.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=4, ensure_ascii=False)
