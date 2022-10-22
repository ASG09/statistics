from DataCapture import DataCapture
import pytest


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
    
    def test_type_error_str_one(self):
        with pytest.raises(TypeError):
            self.capture.add('a')
    def test_type_error_str_two(self):
        with pytest.raises(TypeError):
            self.stats.less('a')
    def test_type_error_str_three(self):
        with pytest.raises(TypeError):
            self.stats.between('a', 1)
    def test_type_error_str_four(self):
        with pytest.raises(TypeError):
            self.stats.less('a')

    def test_type_error_floa_one(self):
        with pytest.raises(TypeError):
            self.capture.add(1.1)
    def test_type_error_float_two(self):
        with pytest.raises(TypeError):
            self.stats.less(1.1)
    def test_type_error_float_three(self):
        with pytest.raises(TypeError):
            self.stats.between(1.1, 1)
    def test_type_error_float_four(self):
        with pytest.raises(TypeError):
            self.stats.greater(1.1)
