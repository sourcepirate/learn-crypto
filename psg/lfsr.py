# LFSR is intended for hardware.
# LFSR - Linear Feedback shift register
# Used for encrypting dvd's and GSM

# LFSR - used in DVD-CSS, GSM-A5, Bluetooth - E0

import os

# taps on 16 14 13 11

def lfsr(start_state, taps=(0, 2, 3, 5)):
    """bit sequence genrators"""
    state = start_state
    while True:
        _gen  = 0
        for tap in taps:
            _gen ^= (state >> tap)
        bit =  _gen & 1
        state = (state >> 1) | (bit << 15)
        yield state

gen = lfsr(0xACE1)
for _ in range(100):
    print(hex(next(gen)))