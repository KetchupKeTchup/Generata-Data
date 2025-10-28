import random
from Countrie import ALL_COUNTRIES
from Person import Person

def generate_users(num_users):
    users = []
    for _ in range(int(num_users)):
        country_data = random.choice(ALL_COUNTRIES)

        person = Person(country_data)
        users.append(person)

    return users



def menu():
    print("\t\t", 40 * "*")
    count = input("\t\t Input how many users to create: ")
    print("\t\t", 40 * "*")

    users_list = generate_users(count)
    print("\n\t\t --- Згенеровані Користувачі ---")
    for i, user in enumerate(users_list[:5]):
        print(
            f"\t\t {i + 1}. {user.name} ({user.age}, {user.countrie}, {user.profession}) - Зарплата: {round(user.salary)} {user.country_data['currency']}")
        # ... тут буде код експорту у Pandas/CSV/JSON ...


if __name__ == "__main__":
    menu()

