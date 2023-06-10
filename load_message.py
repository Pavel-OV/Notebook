import os.path
import json



def load_message():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as f:
            message =json.load(f)
    else:
        message = {"notes": []}
    return message

