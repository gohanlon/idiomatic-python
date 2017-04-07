import os

try:
    os.remove('somefile.tmp')
except OSError:
    pass
