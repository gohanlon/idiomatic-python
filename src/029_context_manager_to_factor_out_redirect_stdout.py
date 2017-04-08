from contextlib import contextmanager

import sys

@contextmanager
def redirect_stdout(fileobj):
    oldstdout = sys.stdout
    sys.stdout = fileobj
    try:
        yield fileobj
    finally:
        sys.stdout = oldstdout

with open('data/help.txt', 'w') as f:
    with redirect_stdout(f):
        help(pow)
