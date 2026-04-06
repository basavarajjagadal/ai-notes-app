def add_note(note):
    with open("notes.txt", "a") as f:
        f.write(note + "\n")

add_note("First Note")