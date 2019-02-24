from typing import Iterable
from entities.purchase import Purchase
from entities.customer import Customer
from entities.product import Product
from value_items.purchase_status_change import PurchaseStatusChange
from logging import log, ERROR
import dateutil.parser


class TabDelimParserService:
    def parse_file(self, file) -> Iterable[Purchase]:
        try:
            # note this is easier with Pandas, but Alpine docker images have trouble with that!
            with open(file) as f:
                rows = f.readlines()
                for raw_row in rows:
                    row = raw_row.split('\t')
                    customer = Customer()
                    customer.id = int(row[0])
                    customer.first_name = row[1]
                    customer.last_name = row[2]
                    customer.address = row[3]
                    customer.state = row[4]
                    customer.zip_code = str(row[5])

                    status = PurchaseStatusChange.canceled if row[6] == 'canceled' else PurchaseStatusChange.new

                    product = Product()
                    product.id = int(row[7])
                    product.name = row[8]

                    purchase = Purchase()
                    purchase.customer = customer
                    purchase.product = product
                    purchase.status_change = status
                    purchase.amount = float(row[9])
                    purchase.datetime = dateutil.parser.parse(row[10])

                    yield purchase
        except Exception as e:
            log(ERROR, '', e)
            yield None
