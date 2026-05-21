# Make a game that generates a time period and the user needs to time it as close as possible

import time
import random

def game():
    print('Waiting Game')

    target_time = round(random.uniform(2.0, 7.0), 2)
    print(f'Your target time is {target_time} second')
    
    input('Press enter to start')
    start_time = time.time()
    print('Time started!')

    input()
    end_time = time.time()

    elapsed_time = round(end_time - start_time, 3)
    diffrence = round(elapsed_time - target_time, 3)
    
    print(' --RESULTS-- ')
    print(f' Time elapsed: {elapsed_time}')
    
    if diffrence == 0:
        print('YOU WIN!')
    elif diffrence >= 0:
        print(' To slow!')
        print(f' You were overshot by {diffrence} seconds!')
    else:
        print(' To fast!')
        print(f' You were undershot by {diffrence} seconds!')

game()