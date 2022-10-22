from DataCapture import DataCapture


class TestDataCapture:

    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()
    
    def test_less(self):
        # should return 2 (only two values 3, 3 are less than 4)
        assert (self.stats.less(4) == 2)

    def test_between(self):
        # should return 4 (3, 3, 4 and 6 are between 3 and 6)
        assert (self.stats.between(3, 6) == 4)

    def test_greater(self):
        # should return 2 (6 and 9 are the only two values greater than 4)
        assert (self.stats.greater(4) == 2)