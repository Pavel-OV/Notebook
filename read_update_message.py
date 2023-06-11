import class_notes as cn
import navigation as nv
import load_save_message as lm

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

def update_message():
     indentifier=input("Найти ппо id, по заголовку либо по тексту \n")
     for notes_elmiment in nv.message["notes"]:
        if indentifier in str(notes_elmiment["id"] ) or indentifier in notes_elmiment["heading"]\
            or indentifier in notes_elmiment["note_body"]:
            heading = input(f"Редактируем заголовок ({notes_elmiment['heading']}): ")
            note_body = input(f"Редактируем сообщение ({notes_elmiment['note_body']})  ")
            notes_elmiment["heading"] = heading or notes_elmiment["heading"]
            notes_elmiment["note_body"] = note_body or notes_elmiment["note_body"] 
            notes_elmiment["last_modified_time"] = str(cn.datetime.now())
            lm.save_message(nv.message)
            print(f"Запись '{notes_elmiment['heading']}'обновлена")
            return
        print(f"Такой '{indentifier}' записи нет")
            
