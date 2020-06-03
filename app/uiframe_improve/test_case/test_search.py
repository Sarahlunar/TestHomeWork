import pytest
import yaml

from app.uiframe_improve.pages.app import App


class TestSearch:
    @pytest.mark.parametrize("stock_name, stock_code", yaml.safe_load(open("..\datas\params\stocks.yaml", encoding="utf-8")) )
    def test_add_stock(self, stock_name, stock_code ):
        app = App()
        opt = app.start().index().goto_quotes().goto_search().search(stock_name, stock_code )
        if opt.is_add(stock_code):
            opt.reset(stock_code)
        opt.add_my_stock(stock_code)

        assert opt.is_add(stock_code)