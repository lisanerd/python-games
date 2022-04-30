
from Hourglass import main as main_h
from Forest_Fire_Sim  import main as main_f
from Rainbow import rainbow
from Rotating_Cube import cube
from Sine_Message import sine_message

print('All my python projects in one code...')


GAMES = ['HOURGLASS', 'FOREST FIRE SIM', 'RAINBOW', 'CUBE', 'SINE MESSAGE']


print()
print('(H) HOURGLASS')
print('(F) FOREST_FIRE_SIM')
print('(R) RAINBOW')
print('(C) CUBE')
print('(S) SINE_MESSAGE')
print()
print('Choose one...')

response = input('> ').upper()



if response == 'H':
    main_h()

elif response == 'F':
    main_f()

elif response == 'R':
    rainbow()

elif response == 'C':
    cube()

elif response == 'S':
    sine_message()