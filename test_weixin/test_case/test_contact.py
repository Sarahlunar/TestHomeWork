from test_weixin.pages.app import App


class TestContact:
    def setup(self):
        self.app = App()
        self.index = self.app.start().index()

    def test_add_member(self):
        message = self.index.goto_addresslist().add_member().mamul_add().\
            input_name().set_gender().input_phonenum().click_save().get_toast()
        assert "成功" in message