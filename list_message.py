import navigation as nv
import class_notes as cn
def list_message():
    for notes_elmiment in nv.message["notes"]:
        notes = cn.Notes.from_dict(notes_elmiment)
        print(notes.id,notes.heading,notes.note_body )
        print()
        print(notes.time_of_creation),        
        print(notes.last_modified_time)
        print()