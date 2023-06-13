import create_delete_message as cm
import load_save_message as lm
import list_message as lst
import read_update_message as rm


def main():
    global message
    message = lm.load_message()
    while True:
        choice = command_selection()
        if choice == 1:
           cm.create_message()
        elif choice == 2:
            rm.read_note()
        elif choice == 3:
            rm.update_message()
        elif choice == 4:
            cm.delete_message()
        elif choice == 5:
            lst.data_note()
        elif choice == 6:
            lst.list_message()
        elif choice == 7:
            print("Программа закрылась. Жду новых записей.")
            break
        
        else:
            print("Не правильно выбрана команда")


def command_selection():
    try:
        choice = int(input("""Выбери действие, нажми
    '1' - создание новой записи   '2' - просмотр  записи
    '3' - изменить запись         '4' - удалить запись
    '5' - поиск по дате создания либо изменения
    '6' - просмотреть все записи  '7' - выход:  \n """))
        return choice
    except ValueError:
        print('Это должно быть число\n')
        
        return command_selection()
        
       

