from datetime import datetime
import os.path
import json
class Notes:
   

    def __init__(self,id,heading, note_body, time_of_creation, last_modified_time):
        self.id =id
        self.heading = heading
        self.note_body = note_body
        self.time_of_creation = time_of_creation
        self.last_modified_time = last_modified_time
        #datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    def to_dict(self):
    	return {
        "id": self.id,
        "heading": self.heading,
        "note_body": self.note_body,
        "time_of_creation":  self.time_of_creation,
        "last_modified_time": self.last_modified_time    }
    @classmethod
    def from_dict(cls,d):
        return cls(
            id= d["id"],
            heading = d["heading"],
            note_body = d["note_body"],
            time_of_creation =(d["time_of_creation"]),
            last_modified_time =(d["last_modified_time"]),
                )
    

    def __repr__(self):
        return f"<Note {self.heading} ({self.id})>"

