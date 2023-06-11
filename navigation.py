import create_delete_message as cm
import load_save_message as lm
import list_message as lst


def main():
    global message
    message = lm.load_message()
    while True:
        choice = input("""Выбери действие, нажми
        '1' - создание новой записи
        '2' - просмотр  записи
        '3' - изменить запись
        '4' - удалить запись
        '5' - просмотреть все записи
        '6' - выход:   """)
        if choice == "1":
           cm.create_message()
        if choice == "2":
            pass
        if choice == "3":
            pass
        if choice == "4":
            cm.delete_message()
        if choice == "5":
            lst.list_message()
        if choice == "6":
            break


        # else:
        #     print("Не правильно выбрана команда")
       

