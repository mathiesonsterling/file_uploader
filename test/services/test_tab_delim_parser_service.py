import pytest
import os

from services.tab_delim_parser_service import TabDelimParserService


class TestTabDelimParserService:
    def test_read_test_file(self):
        file = os.path.join(os.getcwd(), '..', 'test_input_file.dat')

        under_test = TabDelimParserService()

        # ACT
        res = list(under_test.parse_file(file))

        # ASSERT
        assert res
        assert len(res) == 5

        assert len([item for item in res if item.status_change_value == 'cancelled']) == 2

        for item in res:
            assert item
            assert item.customer
            assert item.customer.id > 0
            assert item.customer.first_name
            assert item.customer.last_name
            assert item.customer.address
            assert item.customer.state
            assert item.customer.zip_code

            assert item.product
            assert item.product.id > 0
            assert item.product.name

            assert item.amount > 0
            assert item.datetime
