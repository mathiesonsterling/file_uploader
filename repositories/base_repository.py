from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker
from entities.base_entity import BaseEntity


class BaseRepository:
    db_session = None

    def get_session(self) -> session:
        if not self.db_session:
            self.db_session = self.get_db_session()

        return self.db_session()

    @staticmethod
    def get_db_session():
        db_string = "postgres://postgres:password@db:5432/customer_purchases"
        engine = create_engine(db_string)
        db_session = sessionmaker(bind=engine)
        BaseEntity.metadata.create_all(engine)
        BaseEntity.metadata.bind = engine
        return db_session
