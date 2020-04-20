from session import Session
from utils import print_underline


def print_help():
    help_string = ("Press [Enter] to confirm a command:\n"
                   " p - pause timer\n"
                   " r - resume timer\n"
                   " i - information about timer state\n"
                   " q - end session\n"
                   " c <project> - change session to <project>\n"
                   " h - print this screen\n")
    print(help_string)


def end_program(context):
    for session in context.sessions:
        context.sessions[session].end_session()
        print(context.sessions[session])
        print_underline(15, '-')


def pause(session):
    if not(session.timer.is_paused()):
        session.timer.pause()
        print('Paused ' + session.project_name)


def resume(session):
    if session.timer.is_paused():
        print('Resumed ' + session.project_name)
    session.timer.start()


def info(session):
    print(session.project_name)
    print(session.timer.friendly_state_string())


def change_session(context, change_to_project):
    pause(context.sessions[context.curr_project])
    if not change_to_project in context.sessions:
        context.sessions[change_to_project] = Session(change_to_project)
    context.curr_project = change_to_project
    resume(context.sessions[context.curr_project])
    return context


def do_nothing():
    pass
    

def input_not_recognized():
    print('Input not recognized')
    print_help()

    
def input_handler(input_string, context):
    # menu_items = {
    #     'p': partial(pause, sessions[curr_session]),
    #     'r': partial(resume, sessions[curr_session]),
    #     'i': partial(info, sessions[curr_session]),
    #     'q': partial(end_program, sessions),
    #     'c': partial(change_session, sessions, curr_session),
    #     'h': print_help,
    #     '': do_nothing
    # }
    # func = menu_items.get(command, input_not_recognized)
    # func()

    command = input_string[0]
    curr_project = context.curr_project
    session = context.sessions[curr_project]
    
    if command == 'p':
        pause(session)
    elif command == 'r':
        resume(session)
    elif command == 'i':
        info(session)
    elif command == 'c':
        change_to_project = input_string.split()[1]
        context = change_session(context, change_to_project)
    elif command == 'q':
        end_program(context)
    elif command == 'h':
        print_help()
    elif command == '':
        do_nothing()
    else:
        input_not_recognized()
    
    return context
