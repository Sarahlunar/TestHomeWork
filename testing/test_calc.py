import pytest
import yaml

from demo.calc import Calc


# 定义获取数据的类
class YamlData:
    def __init__(self, data_path):
        # 初始话获取到yaml文件中的数据
        with open(data_path) as f:
            self.data = yaml.safe_load(f)

    # 根据name获取到想要的数据 norm或except
    def get_data(self, name):
        return self.data[name]


# 获取数据
add_data = YamlData('../datas/infodatas/add.yaml')
div_data = YamlData('../datas/infodatas/div.yaml')
sub_data = YamlData('../datas/infodatas/sub.yaml')
mul_data = YamlData('../datas/infodatas/mul.yaml')
steps = yaml.dump(YamlData('../datas/stepdatas/calc.yaml'))

# 定义测试类
class TestCalc:
    # 获取到要测试的方法
    def setup(self):
        self.calc = Calc()

    # 测是add的正常数据
    @pytest.mark.parametrize('test_data', add_data.get_data("norm"))
    def calc_add_norm(self, test_data):
        if 'add' in steps:
            result = self.calc.add(test_data['a'], test_data['b'])
        # 因为获取到的结果可能是多位不确定小数，此处用减法，定义精确度0.0001
            assert test_data['res'] - result < 0.0001

    # 测试add异常情况
    @pytest.mark.parametrize('test_data', add_data.get_data("except"))
    @pytest.mark.xfail
    def calc_add_except(self, test_data):
        for step in steps:
            if 'add' in steps:
                self.calc.add(test_data['a'], test_data['b'])

    # 测试div数据正常情况
    @pytest.mark.parametrize('test_data', div_data.get_data("norm"))
    def calc_div_norm(self, test_data):
        if 'div' in steps:
            result = self.calc.div(test_data['a'], test_data['b'])
            assert test_data['res'] - result < 0.0001

    # 测试div异常情况
    @pytest.mark.parametrize('test_data', div_data.get_data("except"))
    @pytest.mark.xfail
    def calc_div_except(self, test_data):
        if 'div' in steps:
            self.calc.div(test_data["a"], test_data["b"])

    # 测试sub数据正常情况
    @pytest.mark.parametrize('test_data', sub_data.get_data("norm"))
    def calc_sub_norm(self, test_data):
        if 'sub' in steps:
            result = self.calc.sub(test_data['a'], test_data['b'])
            assert test_data['res'] - result < 0.0001

    # 测试sub异常情况
    @pytest.mark.parametrize('test_data', sub_data.get_data("except"))
    @pytest.mark.xfail
    def calc_sub_except(self, test_data):
        if 'sub' in steps:
            self.calc.sub(test_data["a"], test_data["b"])

    # 测试mul数据正常情况
    @pytest.mark.parametrize('test_data', mul_data.get_data("norm"))
    def calc_mul_norm(self, test_data):
        if 'mul' in steps:
            result = self.calc.mul(test_data['a'], test_data['b'])
            assert test_data['res'] - result < 0.0001

    # 测试mul异常情况
    @pytest.mark.parametrize('test_data', mul_data.get_data("except"))
    @pytest.mark.xfail
    def calc_mul_except(self, test_data):
        if 'mul' in steps:
            self.calc.sub(test_data["a"], test_data["b"])


if __name__ == '__main__':
    pytest.main(["-vs", "-m", "add or div", "test_calc.py"])
