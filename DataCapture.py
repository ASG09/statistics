def validate_inputs(*args: int) -> None or Exception:
    '''Validates the inputs and returns an exception if not valid
    
    Keyword arguments:
    *args -- the number(s) to be validated
    '''
    for n in args:
        if not isinstance(n, int):
            raise TypeError('inputs must be integers')
        if n < 0 or n >= 1000:
            raise ValueError('inputs must be positive integers bellow 1000')

    if len(args) == 2:
        # specific Stats.between(n,m) validation:
        if args[0] > args[1]:
            raise ValueError('n must be smaller or equal to m') 

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
        validate_inputs(n)
        if n <= 0:
            return 0
        if n > 1000:
            return len(self.data)
        return self.numbersLowerThan[n]

    def between(self, n: int, m: int) -> int:
        '''Compare integers n and m with the data and returns the amount of numbers between them (inclusive).
        
        Keyword arguments:
        n -- the lower number to be queried
        m -- the greater number to be queried
        '''
        validate_inputs(n, m)
        if n > 999 or m < 0:
            return 0
        return (self.greater(n-1) if n > 0 else len(self.data)) - (self.greater(m) if m < 1000 else 0)

    def greater(self, n: int) -> int:
        '''Compare an integer with the data and returns the amount of numbers greater than it (non inclusive).
        
        Keyword arguments:
        n -- the number to be queried
        '''
        validate_inputs(n)
        if n < 0:
            return len(self.data)
        if n >= 1000:
            return 0
        return len(self.data) - self.numbersLowerThan[n+1]


class DataCapture:

    def __init__(self) -> None:
        '''Instantiate a new DataCapture Object with an empty list of data'''
        self.data = []

    def add(self, n: int) -> None:
        '''Adds a positive int to be included on the statistic calculations. Returns None
        
        Keyword arguments:
        n -- the number to be added
        '''
        validate_inputs(n)
        self.data.append(n)

    def build_stats(self) -> Stats:
        '''Builds the possible statistics results and returns a stats instance, to generate the queries'''
        stats = Stats(self.data)
        return stats
