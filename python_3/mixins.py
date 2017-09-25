from collections import Counter, OrderedDict
import logging
import sys

class LoggingDict(dict):
    def __setitem__(self, key, value):
        logging.info('Setting {} to {}'.format(key, value))
        super().__setitem__(key, value)

class OrderedLoggingDict(LoggingDict, OrderedDict):
    pass

class OrderedCounter(Counter, OrderedDict):
    pass

class ReversedIterator:
    def __init__(self, container):
        self.container = container
        self.index = len(self.container)

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index -= 1
        return self.container[self.index]

    def __iter__(self):
        return self

if __name__ == '__main__':
    print(*ReversedIterator(range(10)))
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    l = OrderedLoggingDict()
    l[2] = 2
    l[1] = 3
    print(l)
