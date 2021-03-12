# Takes a list of Inputs to move from State to State using a template method

class StateMachine:
    def __init__(self, initial_state):
        self.current_state = initial_state
        self.current_state.run()

    def run(self):
        assert 0, "run not implemented"
