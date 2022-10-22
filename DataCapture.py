from typing import Dict


class Stats:

    def __init__(self, data: dict) -> None:
        self.data = data

    def less(self, n: int) -> int:
        if not isinstance(n, int):
            raise TypeError('n must be an int')
        return self.data['less'][n]

    def between(self, n: int, m: int) -> int:
        if (not isinstance(n, int) or not isinstance(m, int)):
            raise TypeError('n and m must be int')
        return self.data['between'][n][m]

    def greater(self, n: int) -> int:
        if not isinstance(n, int):
            raise TypeError('n must be an int')
        return self.data['greater'][n]


class DataCapture:

    def __init__(self) -> None:
        self.data = {}
        self.data['less'] = {i: 0 for i in range(1001)}
        self.data['between'] = {i: {j: 0 for j in range(1001)} for i in range(1001)}
        self.data['greater'] = {i: 0 for i in range(1001)}

    def add(self, n: int) -> None:

        if not isinstance(n, int):
            raise TypeError('n must be an int')

        self.data['less'] = {i: ((self.data['less'][i] + 1) if n < i else (self.data['less'][i])) for i in range(1001)}

        self.data['greater'] = {i: ((self.data['greater'][i] + 1) if n > i else (self.data['greater'][i])) for i in range(1001)}

        self.data['between'] = {
            i: {
                j: ((self.data['between'][i][j] + 1) if (n >= i and n <= j) else (self.data['between'][i][j])) for j in range(1001)
            } for i in range(1001)
        }

    def build_stats(self) -> Stats:
        stats = Stats(self.data)
        return stats