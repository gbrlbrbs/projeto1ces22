class Transitions:
    def __init__(self, states, origins):
        assert set(origins).issubset(states)
        self._origins = origins
        self._dests = states
        self._transitions = {origin: {} for origin in self._origins}

    def set(self, origin, dest, key=None, flag=None, callback=None, params=None, **persist):
        assert origin in self._origins
        assert dest in self._dests

        if params is None:
            params = []

        if key is not None:
            self._transitions[origin][('key', key)] = dest, persist, callback, params
        if flag is not None:
            self._transitions[origin][('flag', flag)] = dest, persist, callback, params

    def get(self, origin, trigger_type):
        return [(trigger[1], dest) for (trigger, dest) in self._transitions[origin].items()
                if trigger[0] == trigger_type]
