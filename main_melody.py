melody = [60, 64, 67, 69, 67, 64, 62, 60]

# CALM
for note in melody:
    playNote(note, beats=2, velocity=55)
# TRANSITION - Calm to Happy
rest(1)
# HAPPY - repeat melody 4 times
for repeat in range(4):
    for note in melody:
        playNote(note, beats=0.5, velocity=100)

# INTENSE - repeat melody 8 times
for repeat in range(8):
    for note in melody:
        playNote(note, beats=0.25, velocity=120)

# REFLECTIVE
for note in melody:
    playNote(note, beats=1.5, velocity=60)
    rest(0.5)
    
# FINAL ENDING
playNote(60, beats=4, velocity=40)
