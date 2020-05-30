from app.uiframe.pages.app import App


class TestSearch:
    def test_add_stock(self):
        app = App()
        res = app.start().index().goto_quotes().goto_search().add_my_stock()

        assert res.is_add()