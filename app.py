from notes import load_notes, save_notes
from add_note import add_note
from edit_note import edit_note
from delete_note import delete_note
from filter_notes import filter_notes_by_date
from display_notes import display_notes

def print_menu():
    print("\nВыберите действие:")
    print("1. Просмотр всех заметок")
    print("2. Добавить заметку")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Фильтровать заметки по дате")
    print("6. Выход")

def main():
    notes = load_notes()

    while True:
        print_menu()
        choice = input("Ваш выбор: ")

        if choice == "1":
            display_notes(notes)
        elif choice == "2":
            title = input("Введите заголовок: ")
            content = input("Введите текст заметки: ")
            notes = add_note(notes, title, content)
        elif choice == "3":
            note_id = int(input("Введите ID заметки для редактирования: "))
            new_title = input("Введите новый заголовок: ")
            new_content = input("Введите новый текст заметки: ")
            notes = edit_note(notes, note_id, new_title, new_content)
        elif choice == "4":
            note_id = int(input("Введите ID заметки для удаления: "))
            notes = delete_note(notes, note_id)
        elif choice == "5":
            date = input("Введите дату в формате YYYY-MM-DD для фильтрации: ")
            filtered_notes = filter_notes_by_date(notes, date)
            display_notes(filtered_notes)
        elif choice == "6":
            save_notes(notes)
            print("До свидания!")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
