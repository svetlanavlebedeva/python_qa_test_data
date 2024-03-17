from faker import Faker

# indicate locales and their weights
locales = ['en-US', 'ru-RU', 'ja_JP']
weights = [1, 2, 3]

fake = Faker(locales)
print(fake.locales)
Faker.seed()

# Generate a name based on the provided weights
# en_US - 16.67% of the time (1 / (1 + 2 + 3))
# ru_RU - 33.33% of the time (2 / (1 + 2 + 3))
# ja_JP - 50.00% of the time (3 / (1 + 2 + 3))
for i in range(10):
    print(fake.name())

fake = Faker('ru-RU')