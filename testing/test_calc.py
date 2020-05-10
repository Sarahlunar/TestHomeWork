import pytest
import yaml

from demo.calc import Calc


# 定义获取数据的类
class YamlData:
    def __init__(self, data_path):
        # 初始话获取到yaml文件中的数据
        self.data = yaml.safe_load(open(data_path))

    # 根据name获取到想要的数据 norm或except
    def get_data(self, name):
        return self.data[name]


# 获取到add和div数据
add_data = YamlData('../datas/add.yaml')
div_data = YamlData('../datas/div.yaml')

# 定义测试类


class TestCalc:
    # 获取到要测试的方法
    def setup(self):
        self.calc = Calc()

    # 测是add的正常数据
    @pytest.mark.parametrize('test_data', add_data.get_data("norm"))
    def test_add_norm(self, test_data):
        result = self.calc.add(test_data['a'], test_data['b'])
        # 因为获取到的结果可能是多位不确定小数，此处用减法，定义精确度0.0001
        assert test_data['res'] - result < 0.0001

    # 测试add异常情况,如果多个异常是不是不能传入数据文件的格式?应该单个处理?
    @pytest.mark.parametrize('test_data', add_data.get_data("except"))
    @pytest.mark.xfail
    def test_add_except(self, test_data):
        result = self.calc.add(test_data['a'], test_data['b'])
        # print(result)
        raise TypeError

    # 测试div数据正常情况
    @pytest.mark.parametrize('test_data', div_data.get_data("norm"))
    def test_div_norm(self, test_data):
        result = self.calc.div(test_data['a'], test_data['b'])
        print(result)
        # 因为获取到的结果可能是多位不确定小数，此处用减法，定义精确度0.0001
        assert test_data['res'] - result < 0.0001

    # 测试div异常情况
    @pytest.mark.parametrize('test_data', div_data.get_data("except"))
    @pytest.mark.xfail
    def test_div_except(self, test_data):
        raise ZeroDivisionError


if __name__ == '__main__':
    pytest.main(['-vs'])
