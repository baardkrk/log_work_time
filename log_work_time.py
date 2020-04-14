import argparse
import time

LOG_FILE_NAME = "project_time_worklog.json"

class Session:
    """ 
    Storage object for each work-log entry/session 
    """
    date
    hours_worked
    description






if __name__ == "__main__":
   parser = argparse.ArgumentParser(description='Log work time for a project')
   parser.add_argument('project_name', metavar='name', type=str, help='Name of the project that we\'ll add worktime for')

   args = parser.parse_args()
   name = args.project_name
   print(name)


def start_time():
    start_work_time = time.time()
