import pytest

from repositories.customer_repository import CustomerRepository
from entities.customer import Customer


def create_customer():
    customer = Customer()
    customer.first_name = 'Testy'
    customer.last_name = 'McTesterson'
    customer.state = "NY"
    customer.zip_code = '11213'
    customer.address = '1641 Pacific St 1'

    return customer


class TestCustomerRepository:
    @pytest.mark.integration
    def test_create_customer(self):
        customer = create_customer()

        under_test = CustomerRepository()

        # ACT
        create_res = under_test.create(customer)

        assert create_res.id

        get_res = under_test.get(create_res.id)

        assert get_res
        assert get_res.first_name == create_res.first_name
