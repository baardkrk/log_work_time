from action_implementation import print_help, pause, resume, info, end_session
from functools import partial


def do_nothing():
    pass
    

def input_not_recognized():
    print('Input not recognized')
    print_help()

    
def input_handler(command, timer):
    menu_items = {
        'p': partial(pause, timer),
        'r': partial(resume, timer),
        'i': partial(info, timer),
        'q': partial(end_session, timer),
        'h': print_help,
        '': do_nothing
    }
    func = menu_items.get(command, input_not_recognized)
    return func()
