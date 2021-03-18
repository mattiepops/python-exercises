# A gigasecond is one billion (10**9) seconds.

from datetime import timedelta

gigasecond = timedelta(seconds=10**9)

def add_gigasecond(difference):

    return difference + gigasecond