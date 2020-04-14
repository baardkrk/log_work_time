class Session:
    """ 
    Storage object for each work-log entry/session. For each pause, a penalty
    of 5 minutes is added to the effectivity. This is to account for lost 
    concentration.
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
                  'Effectiveness:\t{}\n'
                  'Message:\n{}\n')
        return string.format(self.date, self.hours_worked, self.pauses, self.effectiveness(), self.description)
