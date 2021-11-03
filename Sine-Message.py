




import math, shutil, sys, time

# get the size of the terminal window:
WIDTH, HEIGHT = shutil.get_terminal_size()
# we can't print to the last column on Windows without it adding a
# newline automatically, so reduce the width by one:
WIDTH -= 1

print('Sine Mesaage, by Al Sweigart al@inventwithpython.com')
print('(Press Ctrl-C to quit.)')
print()
print('What message do you want to display? (Max', WIDTH // 2, 'chars.)')
while True:
    message = input('> ')
    if 1 <= len(message) <= (WIDTH // 2):
        break
    print('Mesage must be 1 to', WIDTH // 2, 'characters long.')


step = 0.0 # the "step" determines how far into the sine wave we are.
# sine goes from -1.0 to 1.0, so we need to change it by a multiplier:
multiplier = (WIDTH - len(message)) / 2
try:
    while True: # main program loop.
        sinOfStep = math.sin(step)
        padding = ' ' * int((sinOfStep + 1) * multiplier)
        print(padding + message)
        time.sleep(0.1)
        step += 0.25 # (!) try changing this to 0.1 or 0.5.
except KeybaordInterrupt:
    sys.exit() # when Ctrl-C is pressed, end the program.