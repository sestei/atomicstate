#!/usr/bin/env python
import random

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

    def __str__(self):
        return self.name


class GroundState(State):
    def __init__(self):
        super(GroundState, self).__init__('GROUND')

    def is_excited(self):
        # this is not physically correct, but makes things easiert :)
        return True

class FailingState(State):
    def __init__(self, name, success_rate):
        self.success_rate = success_rate
        super(FailingState, self).__init__(name)

    def do_we_succeed(self):
        return random.random() < self.success_rate

    def is_excited(self):
        return self.do_we_succeed()

    def excite(self):
        return self.do_we_succeed()
