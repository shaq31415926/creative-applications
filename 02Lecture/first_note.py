# importing the functions from scamp
from scamp import *

# This session, similar to the real world, is where we record and manage our music
s = Session()
# new part in the session which plays the guitar
guitar = s.new_part("guitar")
# you can use this code to get all the different preset options
# print(s.print_default_soundfont_presets())

# specify a midi note number, the volume and duration
#guitar.play_note(45, 1, 0.5)
#guitar.play_note(52, 1, 0.5)
#guitar.play_note(59, 1, 0.5)
#guitar.play_note(57, 1, 0.5)
#guitar.play_note(60, 1, 0.5)

# creating a list with the notes
guitar_notes = [45, 52, 59, 57, 60]
# loop through the list and play notes for each item in the list
for g in guitar_notes:
    guitar.play_note(g, 1, 0.5)




# print(s.print_default_soundfont_presets())
# to play the note we pass the arguments:
# 1. the "MIDI note number",
# this resource might be helpful: https://inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies
# 2. the volume of the sound which ranges from 0 to 1
# 4. the duration (which is in secs if tempo is not set)
#guitar.play_note(40, 1, 5)
#guitar.play_note(40, 1, 5)
#guitar.play_note(40, 1, 5)
#guitar.play_note(40, 1, 5)