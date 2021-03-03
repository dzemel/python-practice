class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """ Initialize starting value """
        self.start = start
        self.inc = start

    def increment(self):
        """ Increment start value by 1 """
        self.inc += 1
        return self.inc

    def reset(self):
        self.inc = self.start
        return self.start
