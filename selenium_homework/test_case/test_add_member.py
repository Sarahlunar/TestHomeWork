from selenium_homework.page.index import Index


class TestAddMember:
    def setup(self):
        self.index = Index

    def test_add_member(self):
        self.index.goto_add_member().add_member()
        m = self.index.goto_add_member().get_member()
        assert 'asarah' in m