import class_notes as cn
import json
import navigation as nv


def create_message():
    heading = input("heading: "),
    note_body = input("note_body: "),
    time_of_creation = cn.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    id = len(nv.message["notes"])+1
    msg= cn.Notes(id,heading,note_body,time_of_creation)
    nv.message["notes"].append(msg.to_dict())
    save_message(nv.message)
    print(f"Запись {heading} создана")

def save_message(message):
    with open("notes.json", "w", encoding='UTF-8') as f:
        json.dump(message, f ,indent=4 ,ensure_ascii=False) 

