from sqlalchemy import Column, ForeignKey, Float, String, Integer, DateTime

from entities.customer import Customer
from entities.base_entity import BaseEntity
from entities.product import Product
from value_items.purchase_status_change import PurchaseStatusChange


class Purchase(BaseEntity):
    def __init__(self):
        self._customer = None
        self._product = None
        self._status_change = None

    __tablename__ = "Purchases"
    id = Column(Integer, primary_key=True)
    amount = Column(Float)
    datetime = Column(DateTime)
    product_id = Column(Integer, ForeignKey('Products.id'))
    customer_id = Column(Integer, ForeignKey('Customers.id'))
    status_change_value = Column(String)

    @property
    def customer(self) -> Customer:
        return self._customer

    @customer.setter
    def customer(self, customer: Customer):
        self._customer = customer
        self.customer_id = customer.id

    @property
    def product(self) -> Product:
        return self._product

    @product.setter
    def product(self, product: Product):
        self._product = product
        self.product_id = product.id

    @property
    def status_change(self) -> PurchaseStatusChange:
        return self._status_change

    @status_change.setter
    def status_change(self, status_change: PurchaseStatusChange):
        self._status_change = status_change
        self.status_change_value = status_change.value


