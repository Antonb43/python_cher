from datetime import datetime

def add_note(notes, title, content):
    new_id = max([note["id"] for note in notes], default=0) + 1  
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_note = {
        "id": new_id,
        "title": title,
        "content": content,
        "timestamp": timestamp
    }
    notes.append(new_note)
    return notes
