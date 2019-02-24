from typing import Optional
from entities.product import Product

from repositories.base_repository import BaseRepository


class ProductRepository(BaseRepository):
    def get(self, product_id: int) -> Optional[Product]:
        if product_id is None:
            return None

        session = self.get_session()
        res = session.query(Product).filter(Product.id == product_id).first()

        return res

    def create(self, product: Product, auto_commit=True) -> Product:
        session = self.get_session()
        session.add(product)

        if auto_commit:
            session.commit()

        return product
