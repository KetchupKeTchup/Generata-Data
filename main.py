import random
import time
from Person import Person
from FileManager import FileManager


file_manager = FileManager()

# def generate_users(num_users):
#     users = []
#     for _ in range(int(num_users)):
#         country_data = random.choice(ALL_COUNTRIES)
#
#         person = Person(country_data)
#         users.append(person)
#
#     return users



def menu():
    while True:
        print("\t", 40 * "*")
        print("\t [1] - Create new user \n"
              "\t [2] - Show statistics \n"
              "\t [0] - Exit")
        print("\t", 40 * "*")
        action = input("Input: ")
        if action == "1":
            star_time = time.time() # Замірювання часу виконання

            count = int(input("\t Input how many users to create: "))
            while count > 0:
                new_user = Person.generate_person()
                file_manager.save_user(new_user.person_accont())
                count -= 1


            #--------------------------
            end_time = time.time()
            result_time = end_time - star_time
            print(f"Added successfully users")
            print(f"{result_time}: sec")

        elif action == "2":
            pass
        elif action == "0":
            break

if __name__ == "__main__":
    menu()

