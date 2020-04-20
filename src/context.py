from session import Session


class Context:
    """
    Context class for capturing program state
    """
    def __init__(self, curr_project, savefile="worklog.json"):
        self.savefile = savefile
        self.sessions = {}
        self.curr_project = curr_project
        self.sessions[curr_project] = Session(curr_project)


    def write_to_file(self):
        self.load_file()
        self.add_current_context_to_file()
        pass


    def load_file():
        pass


    def add_current_context_to_file():
        pass
