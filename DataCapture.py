class Stats:

    def __init__(self, data: list) -> None:
        '''Builds the possible statistics results and returns a stats instance
        
        Keyword arguments:
        data -- a list containing the numbers to be queried
        '''
        self.data = data
        self.numbersLowerThan = {}
        for n in self.data:
            self.numbersLowerThan = {
                i: (
                    (
                        1 if (i not in self.numbersLowerThan or self.numbersLowerThan[i] == None)
                        else (self.numbersLowerThan[i] + 1)
                    ) if n < i
                    else
                    (
                        0 if (i not in self.numbersLowerThan or self.numbersLowerThan[i] == None)
                        else self.numbersLowerThan[i]
                    )
                ) for i in range(1001)
            }

    def less(self, n: int) -> int:
        '''Compare an integer with the data and returns the amount of numbers lower than it (non inclusive).
        
        Keyword arguments:
        n -- the number to be queried
        '''
        if not isinstance(n, int):
            raise TypeError('n must be an int')
        return self.numbersLowerThan[n]

    def between(self, n: int, m: int) -> int:
        '''Compare integers n and m with the data and returns the amount of numbers between them (inclusive).
        
        Keyword arguments:
        n -- the lower number to be queried
        m -- the greater number to be queried
        '''
        if (not isinstance(n, int) or not isinstance(m, int)):
            raise TypeError('n and m must be int')

        return (self.greater((n-1 if n != 0 else 0))) - self.greater(m)

    def greater(self, n: int) -> int:
        '''Compare an integer with the data and returns the amount of numbers greater than it (non inclusive).
        
        Keyword arguments:
        n -- the number to be queried
        '''
        if not isinstance(n, int):
            raise TypeError('n must be an int')
        return len(self.data) - self.numbersLowerThan[n+1]


class DataCapture:

    def __init__(self) -> None:
        self.data = []

    def add(self, n: int) -> None:
        '''Adds an int to be included on the statistic calculations. Returns None
        
        Keyword arguments:
        n -- the number to be added
        '''
        if not isinstance(n, int):
            raise TypeError('n must be an int')
        self.data.append(n)

    def build_stats(self) -> Stats:
        '''Builds the possible statistics results and returns a stats instance, to generate the queries'''
        stats = Stats(self.data)
        return stats
