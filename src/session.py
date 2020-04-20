from utils import truncate
from timer import TimerObject
from datetime import date

class Session:
    """ 
    Storage object for each work-log entry. 
    """
    def __init__(self, project_name):
        self.date = date.today().strftime("%Y-%m-%d")
        self.project_name = project_name
        self.timer = TimerObject()
        self.message = ""
        self.timer.start()


    def end_session(self):
        self.timer.pause()
        self.message = input("Enter a description for work entry '" + self.project_name + "':\n")

        
    def __str__(self):
        string = ('Work session for \'{}\' \t{}\n'
                  'Hours:\t{}\n'
                  'Interruptions:\t{}\n'
                  'Message:\n"{}"\n')
        return string.format(self.project_name,
                             self.date,
                             truncate(self.timer.hours(), 2),
                             self.timer.stop_count,
                             self.message)
