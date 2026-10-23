# CALM - no drums for 16 beats
rest(16)
# TRANSITION - Calm to Happy
rest(1)
# HAPPY - upbeat drums for 16 beats
for repeat in range(3):
    for i in range(4):
        playNote(0, beats=0.5, velocity=90)
        playNote(4, beats=0.5, velocity=65)

# BUILD-UP - final 4 beats of Happy
for i in range(8):
    playNote(0, beats=0.25, velocity=105)
    playNote(4, beats=0.25, velocity=85)

# INTENSE - powerful drums for 12 beats
for repeat in range(6):
    for i in range(4):
        playNote(0, beats=0.25, velocity=120)
        playNote(4, beats=0.25, velocity=100)

# INTENSE - final dramatic build-up
for i in range(8):
    playNote(0, beats=0.25, velocity=120)
    playNote(4, beats=0.25, velocity=110)

# REFLECTIVE - no drums for 16 beats
rest(16)
