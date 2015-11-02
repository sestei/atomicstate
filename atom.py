#!/usr/bin/env python

from state import GroundState()

class IonisationReached(Exception):
    pass

class Atom(object):
    def __init__(self):
        # The ground state should always be a do-nothing, need-nothing state
        self._states = [GroundState()]
        self._energy = 0
        self._target_energy = 0

    @property
    def ground_state(self):
        return self.state(0)

    @property
    def state(self, energy=-1):
        if energy == -1:
            energy = self._energy
        if len(self._states) > energy:
            return self._states[energy]
        else:
            return None

    def add_state(self, state):
        self._states.append(state)

    def is_excited(self):
        return self.state(self._energy).is_excited()

    def excite(self, energy):
        if self._energy == energy:
            return True
        for E in range(self._energy+1, energy+1):
            if self.state(E).excite():
                self._energy += 1
            else:
                return False
        return True

    def decay(self, energy):
        raise NotImplementedError

    def quantum_leap(self, target):
        if target >= len(self._states):
            raise IonisationReached()
        self._target_energy = target

    def observe(self):
        # this might be called periodically from a main loop, checking whether
        # we are in the state that we should be in, and
        # whether we need to do a state transition
        while not self.is_excited():
            self._energy -= 1
        if self._energy < self._target_energy:
            self.excite(self._target_energy)
        elif self._energy > self._target_energy:
            self.decay(self._target_energy)
        
