# CALM - soft background pad
playNote([48, 55, 60], beats=8, velocity=30)
playNote([45, 52, 57], beats=8, velocity=30)
# TRANSITION - Calm to Happy
rest(1)
# HAPPY - 16 beats
for repeat in range(4):
    for note in [72, 76, 79, 76, 74, 77, 79, 72]:
        playNote(note, beats=0.5, velocity=75)

# INTENSE - cinematic tension, 16 beats
for repeat in range(4):
    playNote([36, 43, 48], beats=2, velocity=100)
    playNote([34, 41, 46], beats=2, velocity=110)


# REFLECTIVE - softer, more spacious atmosphere
playNote([48, 52, 55], beats=4, velocity=30)
rest(2)
playNote([45, 48, 52], beats=4, velocity=28)
rest(2)
playNote([48, 52, 55, 60], beats=4, velocity=25)
