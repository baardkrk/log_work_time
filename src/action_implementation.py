from timer import TimerObject
from session import Session
from utils import truncate
from datetime import date

def print_help():
    help_string = ("Press [Enter] to confirm a command:\n"
                   " p - pause timer\n"
                   " r - resume timer\n"
                   " i - information about timer state\n"
                   " q - end session\n"
                   " h - print this screen\n")
    print(help_string)


def end_session(timer):
    hours = timer.hours()
    print('Total logged time this session: ', truncate(hours, 2), ' hours')
    log_message = input("Enter a description for this entry:\n")
    d = date.today().strftime("%Y-%m-%d")
    session = Session(d, hours, timer.stop_count, log_message)
    print(session)
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
