from datetime import datetime

def edit_note(notes, note_id, new_title, new_content):
    for note in notes:
        if note["id"] == note_id:
            note["title"] = new_title
            note["content"] = new_content
            note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            return notes
    return notes  