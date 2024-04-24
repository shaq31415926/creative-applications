from scamp import *

# creating a musical session
s = Session()
drums = s.new_part("drums")
trumpet = s.new_part("trumpet")

# enter some text
text = """
HEY! HEY! HEY! HEY!
HEY! HEY! HEY! HEY!
DA, DUN DUN DA DUN
DUN DUN DA DUN DUN
DUN DUN!
DA DA DA DUN DUN...DA DA DA DA!
"""

# the logic that plays a note based on a converted character number
for char in text:
    print(char)
    print(ord(char))
    if char == "!" or char == " ":
        wait(0.5)
    else:
        drums.play_note(ord(char)-20, 1, 0.25)

