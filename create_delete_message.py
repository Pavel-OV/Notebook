import class_notes as cn
import navigation as nv
import load_save_message as lm


def create_message():
    heading = input("Заголовок сообщения: "),
    note_body = input("Наберите сообщение: "),
    time_of_creation = cn.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    # cn.datetime.now().strftime('%d-%m-%Y %H:%M')
    #  формат создания переменной time_of_creation даты ДД-ММ-ГГ время ЧЧ:ММ 
    last_modified_time =cn.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    id = len(nv.message["notes"])+1
    msg= cn.Notes(id,heading,note_body,time_of_creation,last_modified_time)
    nv.message["notes"].append(msg.to_dict())
    lm.save_message(nv.message)
    print(f"Запись '{heading}' создана")



def delete_message():
    indentifier=input("Удалить по id, по заголовку либо по тексту\n ")
    for notes_elmiment in nv.message["notes"]:
        if indentifier in str(notes_elmiment["id"] ) or indentifier in notes_elmiment["heading"]\
            or indentifier in notes_elmiment["note_body"]:
            nv.message["notes"].remove(notes_elmiment)
            for i, element in enumerate(nv.message["notes"]):
                element["id"] = i+1
            lm.save_message(nv.message)
            print(f"Запись '{notes_elmiment['heading']}' удалена.")
            return
    print(f"Запись '{indentifier}'не найдена")



        


