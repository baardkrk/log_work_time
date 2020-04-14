from utils import truncate

class Session:
    """ 
    Storage object for each work-log entry/session. 
    The effectiveness function is really not finished.
    """
    def __init__(self, date, hours_worked, pauses, description):
        self.date = date
        self.hours_worked = hours_worked
        self.pauses = pauses
        self.description = description


    def effectiveness(self):
        return (self.hours_worked - (self.pauses * 5 / 60)) / self.hours_worked


    def __str__(self):
        string = ('Date: \t{}\n'
                  'Hours:\t{}\n'
                  'Pauses:\t{}\n'
                  'Effectiveness:\t{}%\n'
                  'Message:\n{}\n')
        return string.format(self.date,
                             truncate(self.hours_worked, 2),
                             self.pauses,
                             truncate(self.effectiveness() * 100, 2),
                             self.description)
