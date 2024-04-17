from scamp import *
# create a session
s = Session()


def beat_it(instrument):
    instrument.play_note(40, 1, 0.25)
    instrument.play_note(43, 1, 0.25)
    instrument.play_note(47, 1, 0.25)
    instrument.play_note(55, 1, 0.25)
    instrument.play_note(52, 1, 0.75)
    instrument.play_note(54, 1, 0.5)
    instrument.play_note(52, 1, 0.25)
    instrument.play_note(50, 1, 0.25)
    wait(0.25)
    instrument.play_note(50, 1.0, 0.25)
    wait(0.75)


def top_part():
    trumpet = s.new_part("trumpet")
    #current_clock().tempo = 120

    trumpet.play_note(71, 1, 0.25)
    trumpet.play_note(71, 1, 1.75)
    trumpet.play_note(71, 1, 0.25)
    trumpet.play_note(71, 1, 1.5)
    trumpet.play_note(71, 1, 0.5)

    trumpet.play_note(71, 1, 0.25)
    trumpet.play_note(71, 1, 0.25)
    trumpet.play_note(71, 1, 0.25)

    trumpet.play_note(71, 1, 0.5)

    trumpet.play_note(71, 1, 0.25, "staccato")
    trumpet.play_note(74, 1, 0.5)
    trumpet.play_note(71, 1, 0.25, "staccato")


# select our instrument
brass = s.new_part("brass")

# play both simultaneously
s.fork(top_part)
s.fork(beat_it, args=[brass])

# and we need to add this, so we can play both instruments together
s.wait_forever()
