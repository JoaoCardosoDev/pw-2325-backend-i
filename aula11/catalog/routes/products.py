from fastapi import APIRouter
from faker import Faker
from faker.providers import isbn, currency, lorem

from catalog.models import Product

fake = Faker()
fake.add_provider(isbn)
fake.add_provider(currency)
fake.add_provider(lorem)

router= APIRouter(prefix="/product", tags=["Products"])

@router.get("")
def get_all_products():
    total_rows=20
    result= [
        Product(
            id=fake.isbn10(),
            name=fake.lorem(nr_word=2),
            prive=fake.pricetag(),
            enabled=True,
            sku=100
        )
        for _ in range(total_rows)
    ]