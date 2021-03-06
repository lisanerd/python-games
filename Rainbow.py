


def rainbow():

    import time, sys

    try:
        import bext
    except ImportError:
        print('This program requires the bext module, which you')
        print('can install by following the instructions at')
        print('https://pypi.org/project/Bext/')
        sys.exit()

    print('Rainbow, by Al Sweigart al@inventwithpython.com')
    print('Press Ctrl-C to stop.')
    time.sleep(1)

    indent = 1 # how many spaces to indent
    indentIncreasing = False # whether the indentation is increasing or not

    try:
        while True: # main program loop
            print(' ' * indent, end='')
            bext.fg('random')
            print('hello', end='')
            bext.fg('green')
            print('hello', end='')
            bext.fg('random')
            print('hello', end='')
            bext.fg('blue')
            print('hello', end='')
            bext.fg('random')
            print('hello', end='')
            bext.fg('red')
            print('hello')
            time.sleep(0.05)

            if indentIncreasing:
                # increase the number of spaces
                indent = indent + 1
                if indent == 10:
                    # change direction
                    indentIncreasing = False
            else:
                # decrease the number of spaces
                indent = indent - 1
                if indent == 0:
                    # change direction:
                    indentIncreasing = True
            
            time.sleep(0.02) # add slight pause
    except KeyboardInterrupt:
        sys.exit() # when Ctrl-C is pressed, end the program



# if this program was run (instead of imported), run the game
if __name__ == '__main__':
    try:
        rainbow()
    except KeyboardInterrupt:
        sys.exit()  # when Ctrl-C is pressed, end the program