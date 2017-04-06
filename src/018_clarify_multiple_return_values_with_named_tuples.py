import doctest

from collections import namedtuple

print(doctest.testmod())
# => TestResults(failed=0, attempted=0)
# which is much clearer than (0, 4)

TestResults = namedtuple('TestResults', ['failed', 'attempted'])
print(TestResults(attempted=0, failed=0))
