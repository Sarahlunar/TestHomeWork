import pytest
import yaml

from demo.calc import Calc


class TestCalcImprove:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize("a, b, expect", yaml.safe_load(open("../datas/infodatas/calc", "rb"))["add"])
    def calc_add(self, a, b, expect):
        print(yaml.safe_load(open("../datas/infodatas/calc", "rb"))["add"])
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            result = self.calc.add(a, b)
            assert result - expect < 0.00001
        else:
            with pytest.raises(TypeError):
                self.calc.add(a, b)


if __name__ == '__main__':
    pytest.main()
