from session import Session


class Context:
    """
    Context class for capturing program state
    """
    def __init__(self, curr_project):
        self.sessions = {}
        self.curr_project = curr_project
        self.sessions[curr_project] = Session(curr_project)


    def write_to_file(self):
        pass
