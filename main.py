import random
from Countrie import ALL_COUNTRIES
from Person import Person

def generate_users(num_users):
    users = []
    for _ in range(num_users):
        country_data = random.choice(ALL_COUNTRIES)

        person = Person(country_data)
        users.append(person)

    return users



def menu():
    print("\t\t", 40 * "*")
    count = input("\t\t Input how many users to create: ")
    print("\t\t", 40 * "*")



# if __name__ == "__main__":
#     menu()

