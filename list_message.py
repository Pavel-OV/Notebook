import navigation as nv
import class_notes as cn
def list_message():
    for notes_elmiment in nv.message["notes"]:
        notes = cn.Notes.from_dict(notes_elmiment)
        print(notes.id,notes.heading,notes.note_body )
        print()
        print(notes.time_of_creation),        
        print(notes.last_modified_time)
        print()

def data_note():
    print("Формат поиска просто число \n дата ЧЧ-ММ-ГГ либо ЧЧ-ММ \n время ЧЧ:ММ ")
    print("В отсутствии результата поиска появится меню ")
    indentifier=input("Найти по времени создания либо изменения записи \n")
    for notes_elmiment in nv.message["notes"]:
        if indentifier in str(notes_elmiment["time_of_creation"] ) or indentifier in notes_elmiment["last_modified_time"]:
            note = cn.Notes.from_dict(notes_elmiment)
            print(note.id,note.heading,note.note_body)
            print()
            print(note.time_of_creation)
            print(note.last_modified_time)
            print()
            
    # return  print(f"Такой '{indentifier}' записи нет")
