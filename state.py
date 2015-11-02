#!/usr/bin/env python

class State(object):
    def __init__(self, name):
        self._name = name
        self.setup()

    @property
    def name(self):
        return self._name

    def setup(self):
        # initialise state variables that we will need etc.
        pass

    def is_excited(self):
        # check if state is still excited, return True or False
        raise NotImplementedError

    def excite(self):
        # try to make transistion to this state 
        raise NotImplementedError

    def decay(self, lower):
        # try to make transition down from this state
        raise NotImplementedError


class GroundState(State):
    def __init__(self):
        super(GroundState, self).__init__('GROUND')
    
    def is_excited(self):
        # this is not physically correct, but makes things easiert :)
        return True
