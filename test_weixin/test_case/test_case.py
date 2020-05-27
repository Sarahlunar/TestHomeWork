import pytest
import yaml

from test_weixin.pages.app import App


class TestContact:
    def setup(self):
        self.app = App()
        self.index = self.app.start().index()

    # 测试添加成员+参数化
    @pytest.mark.parametrize("username, gender, mobile", yaml.safe_load(open("../../datas/wexin/member.yaml", "rb")))
    def test_add_member(self, username, gender, mobile):
        message = self.index.goto_addresslist().add_member().mamul_add().\
            input_name(username).set_gender(gender).input_phone_num(mobile).click_save().get_toast()
        assert "成功" in message

    # def test_add_member(self):
    #     message = self.index.goto_addresslist().add_member().mamul_add(). \
    #         input_name().set_gender().input_phone_num().click_save().get_toast()
    #     assert "成功" in message

    # 测试删除成员
    @pytest.mark.parametrize("username", yaml.safe_load(open("../../datas/wexin/del_member.yaml", "rb")))
    def test_delete_member(self, username):
        self.index.goto_addresslist().to_member_profile(username).\
            to_profile_detail().to_edit_member().delete_member()