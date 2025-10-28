import random
from faker import Faker
fake = Faker()

class Person:

    def __init__(self,country_data):
        self.country_data = country_data
        self.countrie = country_data["countrie"]

        # 1. Визначення незалежних\прямих атрибутів
        self.name = random.choice(country_data["names"])
        self.age = random.randint(18,65)
        self.profession = None
        self.salary = None

        # 2. Виклик методів для розрахунку залежних атрибутів
        self._assign_profession()

        # Генерація через Faker
        self.email = fake.email()
        self.phone_number = country_data["phone_code"] + fake.phone_number()



    def _assign_profession(self):
        self.profession = random.choice(list(self.country_data["profession"].keys()))
        salary_detalis = self.country_data["profession"][self.profession]
        self.salary = random.randint(salary_detalis["salary"]["min"], salary_detalis["salary"]["max"])

