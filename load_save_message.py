import os.path
import json



def load_message():
    if os.path.exists("notes.json"):
        with open("notes.json", "r", encoding='UTF-8') as f:
            message =json.load(f)
    else:
        message = {"notes": []}
    return message

def save_message(message):
    with open("notes.json", "w", encoding='UTF-8') as f:
        json.dump(message, f ,indent=4 ,ensure_ascii=False) 

