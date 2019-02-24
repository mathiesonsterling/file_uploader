from typing import Optional

from repositories.base_repository import BaseRepository
from sqlalchemy import and_

from entities.customer import Customer


class CustomerRepository(BaseRepository):

    def get(self, customer_id: int) -> Customer:
        session = self.get_session()
        result = session.query(Customer).filter(Customer.id == customer_id).first()

        return result

    def get_by_fields(
            self, first_name: str, last_name: str, address: str, state: str, zip_code: str
    ) -> Optional[Customer]:

        session = self.get_session()
        result = session.query(Customer).filter(
            and_(
                Customer.address == address,
                Customer.first_name == first_name,
                Customer.last_name == last_name,
                Customer.state == state,
                Customer.zip_code == zip_code
            )
        ).first()

        return result

    def create(self, customer: Customer, auto_commit=True) -> Customer:
        session = self.get_session()
        session.add(customer)
        if auto_commit:
            session.commit()

        return customer

