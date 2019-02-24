import pytest
from datetime import datetime

from repositories.purchase_repository import PurchaseRepository
from repositories.product_repository import ProductRepository
from repositories.customer_repository import CustomerRepository
from entities.purchase import Purchase
from entities.product import Product
from value_items.purchase_status_change import PurchaseStatusChange
from test.repositories.test_customer_repository import create_customer


def create_purchase():
    product = Product()
    product.name = 'Widget'
    product.id = 1
    test_purchase = Purchase()
    test_purchase.customer = create_customer()
    test_purchase.product = product
    test_purchase.amount = 99.99
    test_purchase.datetime = datetime.now()
    test_purchase.status_change = PurchaseStatusChange.new
    return test_purchase


class TestPurchaseRepository:
    @pytest.mark.integration
    def test_create_purchase(self):
        customer_repo = CustomerRepository()
        product_repo = ProductRepository()

        under_test = PurchaseRepository(customer_repo, product_repo)

        purchase = create_purchase()

        # ACT
        create_res = under_test.create(purchase)
        assert create_res.id

