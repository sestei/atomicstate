from atom import Atom
from state import FailingState
import time

a = Atom()
a.add_state(FailingState('STATE_1', 0.85))
a.add_state(FailingState('STATE_2', 0.7))
run = 0
while True:
    a.observe()
    time.sleep(1)
    run += 1
    if run == 2:
        a.quantum_leap(2)
