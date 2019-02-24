from dataclasses import dataclass

from entities.purchase import Purchase
from repositories.base_repository import BaseRepository
from repositories.customer_repository import CustomerRepository
from repositories.product_repository import ProductRepository


@dataclass()
class PurchaseRepository(BaseRepository):
    customer_repository: CustomerRepository
    product_repository: ProductRepository

    def create(self, purchase: Purchase) -> Purchase:
        customer = self.customer_repository.get_by_fields(
            purchase.customer.first_name,
            purchase.customer.last_name,
            purchase.customer.address,
            purchase.customer.state,
            purchase.customer.zip_code
        )
        if not customer:
            customer = self.customer_repository.create(purchase.customer)
        purchase.customer = customer

        product = self.product_repository.get(purchase.product.id)
        if not product:
            product = self.product_repository.create(purchase.product)
        purchase.product = product

        session = self.get_session()
        session.add(purchase)
        session.commit()

        return purchase
