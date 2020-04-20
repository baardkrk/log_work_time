from utils import truncate

class Session:
    """ 
    Storage object for each work-log entry. 
    """
    def __init__(self, date, hours_worked, interruptions, description):
        self.date = date
        self.hours_worked = hours_worked
        self.interruptions = interruptions
        self.description = description


    def __str__(self):
        string = ('Date: \t{}\n'
                  'Hours:\t{}\n'
                  'Interruptions:\t{}\n'
                  'Message:\n"{}"\n')
        return string.format(self.date,
                             truncate(self.hours_worked, 2),
                             self.interruptions,
                             self.description)
