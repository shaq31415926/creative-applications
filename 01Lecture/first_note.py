from scamp import *

# This session, similar to the real world, is where we record and manage our music
s = Session()
# new part in the session which plays the cello
cello = s.new_part("cello")

# to play the note we pass the arguments:
# 1. the "MIDI note number",
# this resource might be helpful: https://inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies
# 2. the volume of the sound which ranges from 0 to 1
# 4. the duration (which is in secs if tempo is not set)
cello.play_note(40, 1, 5)