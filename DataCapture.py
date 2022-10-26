class Stats:

    def __init__(self, data: dict) -> None:
        '''Builds the possible statistics results and returns a stats instance
        
        Keyword arguments:
        data -- a dictionary with a list called "values", containing the numbers to be queried
        '''

        self.data = data
        for n in self.data['values']:
            self.data['less'] = {
                i: (
                    (
                        1 if ('less' not in self.data or self.data['less'][i] == None)
                        else (self.data['less'][i] + 1)
                    ) if n < i
                    else
                    (
                        0 if ('less' not in self.data or self.data['less'][i] == None)
                        else self.data['less'][i]
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
        return self.data['less'][n]

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
        return len(self.data['values']) - self.less(n+1)


class DataCapture:

    def __init__(self) -> None:
        self.data = {}
        self.data['values'] = []

    def add(self, n: int) -> None:
        '''Adds an int to be included on the statistic calculations. Returns None
        
        Keyword arguments:
        n -- the number to be added
        '''

        if not isinstance(n, int):
            raise TypeError('n must be an int')
        self.data['values'].append(n)

    def build_stats(self) -> Stats:
        '''Builds the possible statistics results and returns a stats instance, to generate the queries'''

        stats = Stats(self.data)
        return stats
