def filter_notes_by_date(notes, date):
    return [note for note in notes if note["timestamp"].startswith(date)]
