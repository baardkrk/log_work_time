import argparse
from context import Context
from utils import print_underline
from input_handler import input_handler, print_help


LOG_FILE_NAME = "project_time_worklog.json"
    

def input_loop(context):
    print_help()
    
    stop = False
    while (not(stop)):
       _in = input('> ')
       context = input_handler(_in, context)
       if (_in == 'q'):
           context.write_to_file()
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
   input_loop(Context(name))
