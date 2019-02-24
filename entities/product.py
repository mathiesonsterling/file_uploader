from sqlalchemy import Column, Integer, String

from entities.base_entity import BaseEntity


class Product(BaseEntity):
    __tablename__ = "Products"
    id = Column(Integer, primary_key=True)
    name = Column(String)

