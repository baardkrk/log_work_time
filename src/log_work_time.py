import argparse
from timer import TimerObject
from utils import print_underline
from input_handler import input_handler
from action_implementation import print_help

LOG_FILE_NAME = "project_time_worklog.json"
    

def input_loop():
    timer = TimerObject()
    timer.start()
    print_help()
    
    stop = False
    while (not(stop)):
       _in = input('> ')
       input_handler(_in, timer)
       if (_in == 'q'):
           stop = True

    
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
   input_loop()
