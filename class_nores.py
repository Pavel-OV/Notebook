from datetime import datetime

class Notes:
    id =0
    heading = ''
    note_body = ''
    time_of_creation = None

    def __init__(self,heading, note_body):
        self.id =Notes.id+1
        Notes.id +=1
        self.heading
        self.note_body
        self.time_of_creation = datetime.now().strftime('%d-%m-%Y %H:%M:%S')

    def get_id(self):
        return self.id
    
    def get_heading(self):
        return self.heading
    
    def get_note_body(self):
        return self.note_body
    
    def get_time_of_creation(self):
        return self.time_of_creation
    
    def set_id(self,n):
         self.id = n
    
    def set_heading(self,n):
        self.heading = n
    
    def set_note_body(self,n):
        self.note_body = n
    
    def set_time_of_creation(self,n):
       self.time_of_creation = n
    
    def __str__(self):
        info = ''
        info += 'f{self.id}'
        info += 'f{self.neading}; '
        info += 'f{note_body}; '
        info += 'f{self.time_of_creation}'
        return info
    

