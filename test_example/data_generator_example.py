import faker

fake = faker.Faker()


def fake_data(count):
    for i in range(count):
        i += 1
        yield {'name': fake.name(), 'phone': fake.phone_number()}


data = fake_data(10)
print(next(data))
