import pytest

from demo.calc import Calc


class TestCalc:
    def setup(self):
        self.calc = Calc()

    def test_add(self):
        result = self.calc.add(1, 2)
        print(result)
        assert 3 == result

    def test_div(self):
        result = self.calc.div(6, 3)
        assert 2 == result



if __name__ == '__main__':
    pytest.main(['-vs', 'test_pytest.py::TestCalc::test_div'])
