from DataCapture import DataCapture, Stats
import pytest

def build_test_data(data: list[int]) -> list[DataCapture, Stats]:
    '''Instantiate and populate a DataCapture and returns it with a Stats object in a list for testing'''
    capture = DataCapture()
    for n in data:
        capture.add(n)
    stats = capture.build_stats()
    return [capture, stats]

class TestDataCapture:

    [capture, stats] = build_test_data([3,9,3,4,6])
    
    # input validations:
    def test_type_error_str_one(self):
        '''capture.add() must receive an int ("a" is not an int)'''
        with pytest.raises(TypeError):
            self.capture.add('a')

    def test_type_error_float_one(self):
        '''capture.add() must receive an int (1.1 is not an int)'''
        with pytest.raises(TypeError):
            self.capture.add(1.1)

class TestStats:

    [capture1, stats1] = build_test_data([3,9,3,4,6])

    # input validations:
    def test_type_error_str_one(self):
        '''stats1.less() must receive an int ("a" is not an int)'''
        with pytest.raises(TypeError):
            self.stats1.less('a')

    def test_type_error_str_two(self):
        '''stats1.between() must receive integers ("a" is not an int)'''
        with pytest.raises(TypeError):
            self.stats1.between('a', 1)

    def test_type_error_str_three(self):
        '''stats1.greater() must receive an int ("a" is not an int)'''
        with pytest.raises(TypeError):
            self.stats1.greater('a')
    
    def test_type_error_float_one(self):
        '''stats1.less() must receive an int (1.1 is not an int)'''
        with pytest.raises(TypeError):
            self.stats1.less(1.1)

    def test_type_error_float_two(self):
        '''stats1.between() must receive integers (1.1 is not an int)'''
        with pytest.raises(TypeError):
            self.stats1.between(1.1, 1)

    def test_type_error_float_three(self):
        '''stats1.greater() must receive an int (1.1 is not an int)'''
        with pytest.raises(TypeError):
            self.stats1.greater(1.1)

    def test_less_lower_limit(self):
        '''stats1.less() must receive an int n such as 0 <= n < 1000'''
        with pytest.raises(ValueError):
            self.stats1.less(-1)

    def test_less_higher_limit(self):
        '''stats1.less() must receive an int n such as 0 <= n < 1000'''
        with pytest.raises(ValueError):
            self.stats1.less(1000)

    def test_between_lower_limit(self):
        '''stats1.between() must receive integers n such as 0 <= n < 1000'''
        with pytest.raises(ValueError):
            self.stats1.between(-1, 4)

    def test_between_higher_limit(self):
        '''stats1.between() must receive integers n such as 0 <= n < 1000'''
        with pytest.raises(ValueError):
            self.stats1.between(4, 1000)

    def test_between_swiched_args(self):
        '''stats1.between(n, m) must receive integers n and m such as n <= m'''
        with pytest.raises(ValueError):
            self.stats1.between(7, 4)

    def test_greater_lower_limit(self):
        '''stats1.greater() must receive an int n such as 0 <= n < 1000'''
        with pytest.raises(ValueError):
            self.stats1.greater(-1)

    def test_greater_higher_limit(self):
        '''stats1.greater() must receive an int n such as 0 <= n < 1000'''
        with pytest.raises(ValueError):
            self.stats1.greater(1000)
    
    # value tests:
    def test_less_one(self):
        '''Should return 2 (only two values 3, 3 are less than 4)'''
        assert (self.stats1.less(4) == 2)

    def test_between_one(self):
        '''Should return 4 (3, 3, 4 and 6 are between 3 and 6)'''
        assert (self.stats1.between(3, 6) == 4)

    def test_between_two(self):
        '''Should return 4 (3, 3, 4 and 6 are between 3 and 6)'''
        assert (self.stats1.between(3, 6) == 4)

    def test_greater_one(self):
        '''Should return 2 (6 and 9 are the only two values greater than 4)'''
        assert (self.stats1.greater(4) == 2)

    [capture2, stats2] = build_test_data([3, 3, 3, 3])

    def test_less_two(self):
        '''Should return 0 (none are less than 3)'''
        assert (self.stats2.less(3) == 0)

    def test_between_three(self):
        '''Should return 4 (3, 3, 3 and 3 are between 3 and 3)'''
        assert (self.stats2.between(3, 3) == 4)

    def test_between_four(self):
        '''Should return 0 (none are between 4 and 6)'''
        assert (self.stats2.between(4, 6) == 0)

    def test_greater_two(self):
        '''Should return 0 (none are greater than 3)'''
        assert (self.stats2.greater(3) == 0)

    [capture3, stats3] = build_test_data([0, 1, 2, 3, 3, 999, 600, 0, 5])

    def test_less_three(self):
        '''Should return 7 (0, 1, 2, 3, 3, 0 and 5 are less than 500)'''
        assert (self.stats3.less(500) == 7)

    def test_less_four(self):
        '''Should return 0 (none are less than 0)'''
        assert (self.stats3.less(0) == 0)

    def test_between_five(self):
        '''Should return 9 (all are between 0 and 999)'''
        assert (self.stats3.between(0, 999) == 9)

    def test_between_six(self):
        '''Should return 1 (1 is between 1 and 1)'''
        assert (self.stats3.between(1, 1) == 1)

    def test_greater_three(self):
        '''Should return 2 (600 and 999 are greater than 500)'''
        assert (self.stats3.greater(500) == 2)