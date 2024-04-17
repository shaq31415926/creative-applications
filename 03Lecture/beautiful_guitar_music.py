# importing the functions from scamp
from scamp import *

# This session, similar to the real world, is where we record and manage our music
s = Session()


def play_overlayed_music(instrument, notes, volume):
    """This function loops through a list of notes and volumes and overlays them on top of each other
    """
    for n, v in zip(notes, volume):
        instrument.play_note(n, v, 1, blocking=False)
        wait(0.25)


# new part in the session which plays the guitar
guitar = s.new_part("guitar")

# this will loop through the code for ten seconds
while s.time() < 10:
    # set one
    play_overlayed_music(guitar,
                         [45, 52, 59, 57, 60],
                         [0.9, 0.6, 0.8, 0.5, 0.8])
    wait(1.5)
    # set two
    play_overlayed_music(guitar,
                         [43, 52, 59],
                         [0.9, 0.6, 0.8])
    wait(1.25)
    # set three
    play_overlayed_music(guitar,
                         [41, 50, 59, 57, 60],
                         [0.9, 0.6, 0.8, 0.5, 0.8])
    wait(1.5)
    # set four
    play_overlayed_music(guitar,
                         [40, 47, 56, 62],
                         [0.9, 0.6, 0.6, 0.8])
    wait(0.7)
