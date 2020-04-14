from timer import TimerObject
from utils import truncate

def print_help(t=0):
    help_string = ("Press [Enter] to confirm a command:\n"
                   " p - pause timer\n"
                   " r - resume timer\n"
                   " i - information about timer state\n"
                   " q - end session\n"
                   " h - print this screen\n")
    print(help_string)


def end_session(timer):
    hours = truncate(timer.hours())
    print('Total logged time this session: ', hours, ' hours')
    return hours


def pause(timer):
    if not(timer.is_paused()):
        timer.pause()
        print('Paused')


def resume(timer):
    if timer.is_paused():
        print('Resumed')
    timer.start()


def info(timer):
    print(timer.friendly_state_string())


def stop(timer):
    end_session(timer)
    stop = True

    
def do_nothing():
    pass
    

def input_not_recognized():
    print('Input not recognized')
    print_help()

"""
def input_handler(command, timer):
    menu_items = {
        'p': pause,
        'r': resume,
        'i': info,
        'q': end_session,
        'h': print_help,
        '': do_nothing
    }
    func = menu_items.get(command, input_not_recognized())
    return func(timer)
"""


def input_handler(command, timer):
    if command == 'h':
        print_help()
        
    elif command == 'p':
        pause(timer)
                   
    elif command == 'r':
        resume(timer)
            
    elif command == 'i':
        info(timer)
               
    elif command == 'q':
        end_session(timer)
    
    elif command == '':
        do_nothing()
               
    else:
        input_not_recognized()
