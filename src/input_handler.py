from action_implementation import print_help, pause, resume, info, end_session

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
def do_nothing():
    pass
    

def input_not_recognized():
    print('Input not recognized')
    print_help()
    

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
