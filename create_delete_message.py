import class_notes as cn
import navigation as nv
import load_save_message as lm


def create_message():
    heading = input("heading: "),
    note_body = input("note_body: "),
    time_of_creation = cn.datetime.now()
    id = len(nv.message["notes"])+1
    msg= cn.Notes(id,heading,note_body,time_of_creation)
    nv.message["notes"].append(msg.to_dict())
    lm.save_message(nv.message)
    print(f"Запись {heading} создана")



def delete_message():
    indentifier=input("Удалить по заголовку либо по тексту \n")
    for notes_elmiment in nv.message["notes"]:
        if str(notes_elmiment["id"] ) == indentifier or notes_elmiment["note_body"] == indentifier:
            nv.message["notes"].remove(notes_elmiment)
            lm.save_message(nv.message)
            print(f"Запись '{notes_elmiment['note_body']}' удалена.")
            return
    print(f"Запись {indentifier} не найдена")



        


