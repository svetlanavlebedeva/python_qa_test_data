from faker import Faker

faker = Faker()
print(f'name: {faker.name()}')  # name: Arthur Patton
print(f'address: {faker.address()}')  # address: 0638 Larsen Way, Tylermouth, CA 48344
print(f'text: {faker.sentence()}')  # text: While per budget up technology design.


faker_ru = Faker('ru_RU')

# Russian data
print(f'Russian name: {faker_ru.name()}')  # Russian name: Иванов Иван Иванович
print(f'Russian address: {faker_ru.address()}')  # Russian address: 196018, ул. Чернышевского, д. 8, кв. 81
print(f'Russian text: {faker_ru.sentence()}')  # Russian text: В конце концов, некоторые отвлеченные факты должны оставаться тайной.

# You can generate more types of data with Russian locale using faker_ru object
print(f'Russian phone number: {faker_ru.phone_number()}')  # Russian phone number: +7 (910) 123-45-67
print(f'Russian job: {faker_ru.job()}')  # Russian job
print(f'Russian company: {faker_ru.company()}')