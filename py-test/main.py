#! /usr/bin/python3

import signal
import time, os
from pprint import pprint

def callme(num, frame):
    pprint(frame, indent=4)
    print("py: callme() called with signal %d" % num, flush=True)
    pass

# register the callback:
signal.signal(signal.SIGTERM, callme)

print("py: Hi, I'm %d, talk to me with 'kill -SIGTERM %d'"
      % (os.getpid(),os.getpid()), flush=True)

# wait for signal info:
while True:
    siginfo = signal.sigwaitinfo({signal.SIGTERM})
    pprint(siginfo, indent=4)
    print("py: waiting for next signal...", flush=True)