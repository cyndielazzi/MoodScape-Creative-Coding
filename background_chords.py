# CALM - 16 beats
playNote([48, 52, 55], beats=4, velocity=45)
playNote([45, 48, 52], beats=4, velocity=45)
playNote([53, 57, 60], beats=4, velocity=45)
playNote([55, 59, 62], beats=4, velocity=45)
# TRANSITION - Calm to Happy
rest(1)
# HAPPY - 16 beats
for repeat in range(4):
    playNote([48, 52, 55], beats=1, velocity=85)
    playNote([55, 59, 62], beats=1, velocity=85)
    playNote([57, 60, 64], beats=1, velocity=85)
    playNote([53, 57, 60], beats=1, velocity=85)

# INTENSE - 16 beats
for repeat in range(8):
    playNote([48, 51, 55], beats=0.5, velocity=110)
    playNote([46, 50, 53], beats=0.5, velocity=110)
    playNote([48, 51, 55], beats=0.5, velocity=110)
    playNote([46, 50, 53], beats=0.5, velocity=110)

# REFLECTIVE - 16 beats
playNote([48, 52, 55], beats=4, velocity=45)
playNote([45, 48, 52], beats=4, velocity=45)
playNote([53, 57, 60], beats=4, velocity=45)
playNote([55, 59, 62], beats=4, velocity=45)

# FINAL ENDING - soft piano chord
playNote([48, 52, 55, 60], beats=4, velocity=35)
