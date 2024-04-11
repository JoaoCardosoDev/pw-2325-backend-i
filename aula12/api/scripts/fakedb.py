from faker import Faker
from api.models import Product


if __name__=="__main__":



fake = Faker()



total_rows=20

    result = [
        Product(
            id=fake.isbn10(),
            name=" ".join(fake.words(nb=2)),
            price=fake.pricetag(),
            enabled=True,
            sku=100
        )
        for _ in range(total_rows)
    ]