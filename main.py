import random
import time
from Person import Person
from FileManager import FileManager
from Countrie import ALL_COUNTRIES


file_manager = FileManager()
def statistics():
    while True:
        print("\t", 40 * "*")
        print("\t [1] - 1 \n"
              "\t [2] - 2 \n"
              "\t [3] - 3 \n"
              "\t [4] - 4 \n"
              "\t [0] - Exit")
        print("\t", 40 * "*")
        
        action = input("\t Input: ")
            
        if action == "1":
            pass
        elif action == "0":
            break
            
        
        

def menu():
    while True:
        print("\t", 40 * "*")
        print("\t [1] - Create new user \n"
              "\t [2] - Show statistics \n"
              "\t [3] - Show countries  \n"
              "\t [4] - Clean users     \n"
              "\t [5] - Users statistics     \n"
              "\t [0] - Exit")
        print("\t", 40 * "*")
        action = input("\t Input: ")
        print("\t", 20 * "-")
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
            print("\t", 40 * "-")
            print(f"\t Added successfully users")
            print(f"\t {round(result_time,2)}: sec \n")

        elif action == "2":
            file_manager.read_file_users()
        elif action == "3":
            for i in ALL_COUNTRIES:
                print(f"\t{i["countrie"]}, currency: {i["currency"]}, tax_rate: {i["tax_rate"]}, ")
                print("\t-" * 20)
        
        elif action == "4":
            file_manager.cleal_json_file()
            print("\t All users is delete")
            
        elif action == "5":
            statistics()
        
        elif action == "0":
            break
        
        else:
            print("\t Wrong number")

if __name__ == "__main__":
    menu()
