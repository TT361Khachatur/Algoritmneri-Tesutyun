# Վերջավոր ավտոմատներ
class FiniteAutomaton:
    def __init__(self, states, alphabet, transition, start, accepts):
        self.states = states
        self.alphabet = alphabet
        self.transition = transition
        self.start = start
        self.accepts = accepts

    def accepts_string(self, s):
        current = self.start
        for ch in s:
            current = self.transition.get((current, ch))
            if current is None:
                return False
        return current in self.accepts
