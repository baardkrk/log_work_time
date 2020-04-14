import argparse
import time

LOG_FILE_NAME = "project_time_worklog.json"

class Session:
    """ 
    Storage object for each work-log entry/session 
    """
    def __init__(self, date, hours_worked, description):
        self.date = date
        self.hours_worked = hours_worked
        self.description = description


        

def print_help(t=0):
    help_string = ("Press [Enter] to confirm a command:\n"
                   " p - pause timer\n"
                   " r - resume timer\n"
                   " q - end session\n"
                   " h - print this screen\n")
    print(help_string)


def start_timer(resume=False):
    t0 = time.time()
    print('Resumed timer' if resume else 'Started timer')
    return t0


def stop_timer(t, t0):
    t1 = time.time()
    t += t1-t0
    return t


def pause_timer(acc_time, t0):
    acc_time = stop_timer(acc_time, t0)
    hours = seconds_to_hours(acc_time)
    print('Paused timer \t(accumulated: ', truncate(hours, 3), ')')
    return acc_time


def end_session(t, t0):
    acc_time = stop_timer(t, t0)
    hours = truncate(seconds_to_hours(acc_time), 2)
    print('Total logged time this session: ', hours, ' hours')
    return hours


def seconds_to_hours(seconds):
    return seconds / (60*60)
    
    
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier


def print_underline(length, character="="):
    li = []
    for _ in range(length):
        li.append(character)
    underline = ''.join(li)
    
    print(underline, '\n')

    
if __name__ == "__main__":
   parser = argparse.ArgumentParser(description='Log work time for a project')
   parser.add_argument('project_name',
                       metavar='name',
                       type=str,
                       help='Name of the project that we\'ll add worktime for')

   args = parser.parse_args()
   name = args.project_name
   print('Logging hours for', name)
   print_underline(18 + len(name))

   print_help()
   t0 = start_timer()

   stop = False
   paused = False
   acc_time = 0.0
   while (not(stop)):
       _in = input('> ')

       if _in == 'h':
           print_help()
           
       elif _in == 'p':
           if not(paused):
               acc_time = pause_timer(acc_time, t0)
               paused = True
               
       elif _in == 'r':
           if paused:
               t0 = start_timer(resume=True)
               paused = False
           else:
               print('Timer was already resumed')
               
       elif _in == 'q':
           end_session(acc_time, t0)
           stop = True
           
       else:
           print('Input not recognized')
           print_help()
