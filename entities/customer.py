from sqlalchemy import Column, Integer, ForeignKey, String

from entities.base_entity import BaseEntity


class Customer(BaseEntity):
    __tablename__ = 'Customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    state = Column(String)
    zip_code = Column(String)
