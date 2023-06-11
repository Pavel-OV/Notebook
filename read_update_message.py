import class_notes as cn
import navigation as nv

def read_note():
    indentifier=input("Найти ппо id, по заголовку либо по тексту \n")
    for notes_elmiment in nv.message["notes"]:
        if indentifier in str(notes_elmiment["id"] ) or indentifier in notes_elmiment["heading"]\
            or indentifier in notes_elmiment["note_body"]:
            note = cn.Notes.from_dict(notes_elmiment)
            print(note.id,note.heading,note.note_body)
            print()
            print(note.time_of_creation)
            print(note.last_modified_time)
            print()
            return
    return  print(f"Такой '{indentifier}' записи нет")