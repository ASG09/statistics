class Stats:

    def __init__(self, data: dict) -> None:
        self.data = data
        for n in self.data['values']:
            self.data['less'] = {i: ((self.data['less'][i] + 1) if n < i else (self.data['less'][i])) for i in range(1001)}
            self.data['greater'] = {i: ((self.data['greater'][i] + 1) if n > i else (self.data['greater'][i])) for i in range(1001)}

    def less(self, n: int) -> int:
        '''returns the amount of numbers added less than a given number n'''

        if not isinstance(n, int):
            raise TypeError('n must be an int')
        return self.data['less'][n]

    def between(self, n: int, m: int) -> int:
        '''returns the amount of numbers added in between a given number n (inclusive) and m (inclusive)'''

        if (not isinstance(n, int) or not isinstance(m, int)):
            raise TypeError('n and m must be int')

        return self.data['greater'][n-1 if n!=0 else 0] - self.data['greater'][m]

    def greater(self, n: int) -> int:
        '''returns the amount of numbers added greater than a given number n'''

        if not isinstance(n, int):
            raise TypeError('n must be an int')
        return self.data['greater'][n]


class DataCapture:

    def __init__(self) -> None:
        self.data = {}
        self.data['values'] = []
        self.data['less'] = {i: 0 for i in range(1001)}
        self.data['between'] = {i: {j: 0 for j in range(1001)} for i in range(1001)}
        self.data['greater'] = {i: 0 for i in range(1001)}

    def add(self, n: int) -> None:
        '''adds number to be included on the stats data'''

        if not isinstance(n, int):
            raise TypeError('n must be an int')
        self.data['values'].append(n)
        
    def build_stats(self) -> Stats:
        '''creates a stats instance'''

        stats = Stats(self.data)
        return stats