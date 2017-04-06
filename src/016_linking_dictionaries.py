import argparse
import os

defaults = {'color': 'red', 'user': 'guest'}

parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')

namespace = parser.parse_args([])
command_line_args = {k: v for k, v in vars(namespace).items() if v}

d = defaults.copy()
d.update(os.environ)
d.update(command_line_args)

print(d)
