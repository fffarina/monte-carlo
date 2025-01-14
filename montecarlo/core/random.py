from warnings import warn


__all__ = ["Mersenne", "MiddleSqaure"]


class Mersenne:
    """Pseudorandom object generater"""

    def __init__(self, seed=1234):
        """Construct pseudorandom computation attributes"""
        self.seed = seed
        self.j = 2**31 - 1
        self.k = 16807
        self.period = 2**30

    def floating(self, interval=None, count=1):
        """
        Return a pseudorandom float. Default is one floating-
        point number between zero and one. Pass in a tuple or
        list, (a,b), to return a floating-point number on
        [a,b]. If count is 1, a single number is returned,
        otherwise a list of numbers is returned.
        """
        results = []
        if interval is not None:
            start, interval = interval[0], interval[1] - interval[0]
        else:
            start, interval = 0.0, 1.0
        for i in range(count):
            self.seed = (self.k * self.seed) % self.j
            results.append((interval * (self.seed / self.j)) + start)
            self.period -= 1
            if self.period == 0:
                warn("Pseudorandom period warning!!")
        if count == 1:
            return results.pop()
        else:
            return results
    
    def integer(self, interval=None, count=1):
        """
        Return a pseudorandom integer. Default is one integer
        number in {0,1}. Pass in a tuple or list, (a,b), to
        return an integer number on [a,b]. If count is 1, a
        single number is returned, otherwise a list of numbers
        is returned.
        """
        if count == 1:
            return round(self.floating(interval=interval))
        elif count > 1:
            return [
                round(f) for f in self.floating(
                    interval=interval, count=count
                )
            ]
            
    def alpha(self, count=1):
        """
        Return a pseudorandom alphabetical letter (English).
        By default, one letter in a-z is returned. If count is
        greater than 1, a string a length count is returned.
        """
        chars = "abcdefghijklmnopqrstuvwxyz"
        if count == 1:
            return chars[self.integer(interval=(0,25))]
        elif count > 1:
            return "".join(
                chars[f] for f in self.integer(
                    interval=(0,25), count=count
                )
            )


class MiddleSqaure:
    """WIP"""
    pass
