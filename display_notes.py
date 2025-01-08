def display_notes(notes):
    for note in notes:
        print(f"ID: {note['id']}, Title: {note['title']}, Date: {note['timestamp']}")
        print(f"Content: {note['content']}")
        print("-" * 20)
